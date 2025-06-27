import json

with open("q-clean-up-sales-data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

#extract data where product is "Bike" and sales are atleast 9
filter_product = [
    item for item in data if item.get("product") == "Bike" and item.get("sales", 0) >= 9
]

filter_city = [
    item for item in filter_product if item.get("city")[0] == 'K'
]

karachi = ['Karrchi', 'Karachi']

sum = 0
for item in filter_city:
    if item.get("city") in karachi:
        sum += item.get("sales", 0)
print(sum)  # Output the total sales for filtered items


#Output: 2721