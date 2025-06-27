import re
import json

# Load the full text from the file (already provided above)
file_path = "q-clean-up-student-marks.txt"
with open(file_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

# Extract name, ID, and marks using regex
lines = raw_text.strip().split('\n')
data =[]
ids = []

for line in lines:
    if "Marks" in line:
        marks_split = line.split("Marks")
        #before, after = line.split("Marks", 1)
        marks = marks_split[-1].strip()
        before = marks_split[0].strip() + marks_split[1].strip() if len(marks_split) > 2 else marks_split[0].strip()
        before = before.replace(":", "").replace(" ", "")
        splitter = before.split("-")
        data.append({
            "Name": before.strip(),
            "ID": splitter[-1].strip(),
            "Marks": marks
        })
        ids.append(splitter[-1].strip())
        


# Save to a formatted JSON file
output_path = "cleaned_student_data.json"
with open(output_path, "w", encoding="utf-8") as out_file:
    json.dump(data, out_file, indent=2)

output_path  # return path to JSON file

ids = sorted(ids)
print(len(set(ids)))  # Print the number of unique IDs


#Output : 155