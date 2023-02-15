import re

input_str = "CHEM114L-GeneralChemistryIILab"

# Define a regular expression pattern to match the hyphen and the text on either side
pattern = r"^(.+?)-(.+)$"

# Use re.match to search for a match to the pattern in the input string
match = re.match(pattern, input_str)

if match:
    # If a match is found, extract the class code and title from the groups in the match object
    class_code = match.group(1)
    title = re.sub(r"([a-z])([A-Z])", r"\1 \2", match.group(2))

    # Print out the extracted values
    print("Class code: {}".format(class_code))
    print("Title: {}".format(title))
else:
    print("No match found") 