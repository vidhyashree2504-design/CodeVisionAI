import string

# File paths
input_file = "data/raw_data.txt"
output_file = "data/cleaned_data.txt"

cleaned_lines = []

with open(input_file, "r") as file:
    for line in file:
        line = line.lower()  # lowercase
        line = line.strip()  # remove extra spaces
        line = line.translate(str.maketrans("", "", string.punctuation))  # remove punctuation
        
        if line:
            cleaned_lines.append(line)

with open(output_file, "w") as file:
    for line in cleaned_lines:
        file.write(line + "\n")

print("Dataset cleaned successfully!")