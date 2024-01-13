import json

# Create a Python dictionary
python_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
with open('test.txt', 'r+') as f:    
    json_string = json.dump(python_data, f)
    f.readline()

# Print the JSON string
f.closed
