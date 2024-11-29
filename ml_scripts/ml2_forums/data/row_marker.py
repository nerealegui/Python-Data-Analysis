
# Open the file in read mode
with open('otherWords.txt', 'r') as file:
    lines = file.readlines()

# Add "app" in front of each line
modified_lines = ['other ' + line for line in lines]

# Open the file in write mode and save the modified lines
with open('otherWords.txt', 'w') as file:
    file.writelines(modified_lines)

# merge the two files otherWords.txt and appWords.txt into one file called allWords.txt
# Open the otherWords.txt file in read mode
with open('otherWords.txt', 'r') as file:
    other_words = file.readlines()

# Open the appWords.txt file in read mode
with open('appWords.txt', 'r') as file:
    app_words = file.readlines()

# Combine the contents of both files
all_words = other_words + app_words

# Open the allWords.txt file in write mode and save the combined contents
with open('allWords.txt', 'w') as file:
    file.writelines(all_words)



