import json

# Generating JSON:
# Create a Python dictionary
data = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}

# Convert dictionary to JSON string
json_string = json.dumps(data)
print(json_string) # '{"name": "Alice", "age": 25, "city": "London"}'

with open("dict_to_json.json", "w") as file:
    file.write(json_string)

# Parsing JSON:
# Method 1 - Sample JSON data
json_data1 = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON data into a Python dictionary
data1 = json.loads(json_data1)

# Access values
print(data1["name"])
print(data1["age"])

# Method 2 - Read JSON data from a file
with open("dict_to_json.json", "r") as file:  # file object is iterable
    json_data2 = file.read()

# Parse JSON data into a Python dictionary
data2 = json.loads(json_data2)

# Access values
print(data2["name"])
print(data2["age"])
