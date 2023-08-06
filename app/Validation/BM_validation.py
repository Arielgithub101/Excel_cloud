import os

from pydantic import BaseModel, FilePath, DirectoryPath, validator
from starlette.responses import JSONResponse


def validate_file_extension(input_file_path: str):
    # if not input_file_path.lower().endswith('.xlsx'):
    #     raise ValueError("The file path must point to a .xlsx file.")
    if not os.path.exists(input_file_path):
        return JSONResponse(content="Input file does not exist.", status_code=422)
    return input_file_path


class ExcelProcessing(BaseModel):
    input_file_path: str
    new_file_path: str
    new_file_name: str

    @validator('input_file_path')
    def validate_input_file_path(cls, v):
        return validate_file_extension(v)

    @validator('new_file_path')
    def validate_new_file_path(cls, v):
        if not v.lower().endswith('/'):
            v += "/"
        return v
