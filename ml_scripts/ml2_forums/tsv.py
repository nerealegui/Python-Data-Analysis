import pandas as pd

# Read files BillGates.xlsx and ElonMusk.xlsx grab only the variables screen_name and text, and save them in a TSV file. In front of each line, add the string "BillGates" or "ElonMusk" respectively
bill_gates_df = pd.read_excel('/Users/nerea/Documents/Github_Repos/MLSnackBar/python_scripts/ml2_forums/BillGates.xlsx')
elon_musk_df = pd.read_excel('/Users/nerea/Documents/Github_Repos/MLSnackBar/python_scripts/ml2_forums/ElonMusk.xlsx')

# Select the required columns and add a new column for the identifier
bill_gates_df = bill_gates_df[['screen_name', 'text']]


elon_musk_df = elon_musk_df[['screen_name', 'text']]


# Concatenate the dataframes
combined_df = pd.concat([bill_gates_df, elon_musk_df])

# Reorder columns to have the identifier first
combined_df = combined_df[['screen_name', 'text']]

# Save to TSV file
combined_df.to_csv('/Users/nerea/Documents/Github_Repos/MLSnackBar/python_scripts/ml2_forums/muskGates.tsv', sep='\t', index=False)
