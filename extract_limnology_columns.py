import pandas as pd
import os

# Define the main directory containing the 31 lake folders
main_dir = r"S:\Sem_4\Dataset_Temp"  # Path to the dataset folders
output_file = r"S:\Sem_4\Scripts\lake_limnology_columns.xlsx"  # Output in the scripts directory

# Sheet name to process
sheet_name = "Limnology"

# List to store lake names and their column names lists
lake_columns = []

# Variable to track the maximum number of columns
max_cols = 0

# Iterate through each folder in the main directory
for lake_folder in os.listdir(main_dir):
    lake_path = os.path.join(main_dir, lake_folder)
    if os.path.isdir(lake_path):
        # Transform the folder name to match the file naming convention: uppercase, spaces to underscores
        lake_name_transformed = lake_folder.upper().replace(" ", "_")
        # Construct the expected Excel file name
        excel_file = f"{lake_name_transformed}_WQ_ANALYSIS.xlsx"
        excel_path = os.path.join(lake_path, excel_file)

        if os.path.exists(excel_path):
            # Read the Limnology sheet from the Excel file
            try:
                df = pd.read_excel(excel_path, sheet_name=sheet_name)
                # Get the list of column names
                columns_list = df.columns.tolist()
                # Update max_cols if this lake has more columns
                if len(columns_list) > max_cols:
                    max_cols = len(columns_list)
                # Append to the list as a dict for now
                lake_columns.append({"Lake_Name": lake_folder, "Columns": columns_list})
            except ValueError:
                print(f"Sheet '{sheet_name}' not found in {excel_file}")
        else:
            print(f"Excel file not found: {excel_path}")

# Now, prepare the data for the wide format DataFrame
if lake_columns:
    # Create column headers
    headers = ["Lake_Name"] + [f"Column_Name_{i + 1}" for i in range(max_cols)]

    # Create rows
    rows = []
    for lake in lake_columns:
        # Pad the columns list with empty strings if shorter than max_cols
        padded_columns = lake["Columns"] + [""] * (max_cols - len(lake["Columns"]))
        row = [lake["Lake_Name"]] + padded_columns
        rows.append(row)

    # Create DataFrame
    columns_df = pd.DataFrame(rows, columns=headers)

    # Write to Excel
    with pd.ExcelWriter(output_file) as writer:
        columns_df.to_excel(writer, sheet_name="Limnology_Columns", index=False)
    print(f"Excel file with column names saved as {output_file}")
else:
    print("No data found to process.")