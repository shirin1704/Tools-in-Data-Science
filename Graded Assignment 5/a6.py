import json

'''input_file = "q-parse-partial-json.jsonl"
output_file = "a6_cleaned_data.json"

sales = 0

with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
    for i, line in enumerate(fin, 1):
        line = line.strip()

        # Try parsing as-is
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            # Try appending a closing brace
            try:
                if line.endswith("\""):
                    obj = json.loads(line + "}")
                else:
                    obj = json.loads(line + "\"}")
            except json.JSONDecodeError:
                print(f"Line {i} is too corrupted to fix: {line}") 
                continue

        # Write cleaned line
        fout.write(json.dumps(obj) + "\n")

print(f"Cleaned lines written to: {output_file}")'''

sum = 0
with open('a6_cleaned_data.json', "r", encoding="utf-8") as file:
    data = json.load(file)

for line in data:
    sum = sum + line['sales']

print(sum)

#output:52905