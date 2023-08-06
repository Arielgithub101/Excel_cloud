import pandas as pd

# Replace 'input_file_path.xls' with the actual path to your input Excel file
input_file_path = 'C:/Users/mamag4/Desktop/Book1.xlsx'

# Replace 'output_file_path.xls' with the desired path for the new Excel file
new_file_path = 'C:/Users/mamag4/Desktop/new_file_path3.xlsx'

# Read the Excel file into a DataFrame using the 'xlrd' engine
df = pd.read_excel(input_file_path, header=None)

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

# Save the modified DataFrame to a new Excel file
df.to_excel(new_file_path, index=False)

print("finish")

#
# import os
#
# import pandas as pd
#
#
# def process_excel(input_file_path, new_file_path, new_file_name):
#     if not os.path.exists(input_file_path):
#         raise ValueError("Input file does not exist.")
#         # Read the Excel file into a DataFrame using the 'xlrd' engine
#     df = pd.read_excel(input_file_path, header=None)
#
#     # Specify the columns to check (B, C, and D)
#     columns_to_check = df.iloc[:, 1:4]
#
#     # Iterate over all rows and columns
#     for index, row in df.iterrows():
#         for column in columns_to_check:
#             cell_value = row[column]
#             if -1 <= cell_value <= 1:
#                 # If any value in columns B, C, or D is between -1 and 1, set all three cells to 0
#                 df.at[index, 1] = 0
#                 df.at[index, 2] = 0
#                 df.at[index, 3] = 0
#
#     suffix = '.xlsx'
#     new_file_path = new_file_path + (new_file_name + suffix)
#     if os.path.exists(new_file_path):
#         raise ValueError("file name is already exists.")
#
#     # Save the modified DataFrame to a new Excel file
#     df.to_excel(new_file_path, index=False)
#     return new_file_path
