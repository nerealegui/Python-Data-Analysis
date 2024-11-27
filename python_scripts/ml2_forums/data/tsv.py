# Read the content of the file
with open('allWords', 'r') as file:
    lines = file.readlines()

# Transform each line to TSV format
tsv_lines = [line.replace(' ', '\t', 1) for line in lines]

# Write the transformed content to a new TSV file
with open('allWords.tsv', 'w') as file:
    file.writelines(tsv_lines)