import pandas as pd
import os

# Define the main directory containing the 31 lake folders
main_dir = r"S:\Sem_4\Dataset_Temp_v1"  # Path to the dataset folders
output_file = r"S:\Sem_4\Scripts\merged_limnology_data.xlsx"  # Output in the scripts directory

# Sheet name to process
sheet_name = "Limnology"

# List to store DataFrames for the Limnology sheet
limnology_dfs = []

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
                # Add a column for the lake name (using original folder name for readability)
                #df["Lake_Name"] = lake_folder
                # Append the DataFrame to the list
                limnology_dfs.append(df)
            except ValueError:
                print(f"Sheet '{sheet_name}' not found in {excel_file}")
        else:
            print(f"Excel file not found: {excel_path}")

# Combine all DataFrames for the Limnology sheet and write to a new Excel file
if limnology_dfs:
    combined_df = pd.concat(limnology_dfs, ignore_index=True)
    with pd.ExcelWriter(output_file) as writer:
        combined_df.to_excel(writer, sheet_name=sheet_name, index=False)
    print(f"Merged Excel file saved as {output_file}")
else:
    print("No data found to merge.")