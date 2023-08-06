import os
import pandas as pd

from fastapi import APIRouter
from app.Validation.BM_validation import ExcelProcessing
from starlette.responses import JSONResponse

router = APIRouter(
    prefix="/process_excel"
)


@router.post("/")
async def process_excel_route(ecxel: ExcelProcessing):
    try:
        # Read the Excel file into a DataFrame using the 'xlrd' engine
        df = pd.read_excel(ecxel.input_file_path, header=None)

        # Specify the columns to check (B, C, and D)
        columns_to_check = df.iloc[:, 1:4]

        # Iterate over all rows and columns
        for index, row in df.iterrows():
            for column in columns_to_check:
                cell_value = row[column]
                if -1 <= cell_value <= 1:
                    # If any value in columns B, C, or D is between -1 and 1, set all three cells to 0
                    df.at[index, 1] = 0
                    df.at[index, 2] = 0
                    df.at[index, 3] = 0

        suffix = '.xlsx'
        new_path = ecxel.new_file_path + (ecxel.new_file_name + suffix)

        if os.path.exists(new_path):
            return JSONResponse(content="file name is already exists.", status_code=404)

        # Save the modified DataFrame to a new Excel file
        df.to_excel(new_path, index=False)
        return JSONResponse(content={"message": "new file created successfully", "path file": new_path},
                            status_code=200)
    except ValueError as e:
        error_respose = {"error": str(e)}
        return JSONResponse(content=error_respose, status_code=500)
