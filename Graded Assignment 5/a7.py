import json

def count_blr_keys(obj):
    count = 0
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "BLR":
                count += 1
            count += count_blr_keys(value)  # Recursively check nested content
    elif isinstance(obj, list):
        for item in obj:
            count += count_blr_keys(item)
    return count

# Load the JSON file
with open("q-extract-nested-json-keys.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Count how many times "blr" appears as a key
blr_key_count = count_blr_keys(data)

print(f'The key "blr" appears {blr_key_count} time(s).')

#output : 28227