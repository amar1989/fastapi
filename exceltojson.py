import xlrd
import json

import xlrd
import json

def convert_xls_to_json(xls_file_path, json_file_path):
    """
    Convert an .xls file to a .json file.

    Parameters:
        xls_file_path (str): Path to the input Excel (.xls) file.
        json_file_path (str): Path to the output JSON file.

    Returns:
        None
    """
    try:
        # Open the workbook using xlrd
        workbook = xlrd.open_workbook(xls_file_path)

        # Select the first sheet
        sheet = workbook.sheet_by_index(0)

        # Extract data from the sheet
        data = []
        headers = [sheet.cell_value(0, col) for col in range(sheet.ncols)]  # First row as headers
        for row_idx in range(2, sheet.nrows):
            row_data = {
                "MEM NO": int(sheet.cell_value(row_idx, 1)),
                "MEMBER NAME": sheet.cell_value(row_idx, 2),
                "CATEGORY": sheet.cell_value(row_idx, 3)
            }
            data.append(row_data)

        # Write the data to a JSON file
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"Successfully converted {xls_file_path} to {json_file_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
xlsx_file_path = '/Users/amarsingh/Downloads/NDSmembers.xls'  # Replace with your Excel file path
json_file_path = 'output_file.json'  # Replace with your desired JSON file path
convert_xls_to_json(xlsx_file_path, json_file_path)