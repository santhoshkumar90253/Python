''' Nested Data Structure Flattener
 • Concepts: Handling nested dictionaries/lists, recursion or iterative approaches, and data 
transformation using comprehensions.
 • Description:
 Create a script that accepts a nested dictionary (for example, loaded from a JSON file) and 
flattens it into a single-level dictionary. Use a separator (like an underscore) to concatenate 
nested keys into new single keys.
 • Validation:
 Use a sample nested structure to verify that the output dictionary correctly maps all nested 
values to single-level keys.'''
import json

def flatten(data, parent_key='', sep='_'):
    flat_dict = {}
    if isinstance(data, dict):
        for key, value in data.items():
            full_key = f"{parent_key}{sep}{key}" if parent_key else key
            flat_dict.update(flatten(value, full_key, sep))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            full_key = f"{parent_key}{sep}{i}"
            flat_dict.update(flatten(item, full_key, sep))
    else:
        flat_dict[parent_key] = data
    return flat_dict

json_filename=input("Enter the json file:")
with open(json_filename, "r") as f:
    nested_data = json.load(f)

flat_data = flatten(nested_data)
for i,j in flat_data.items():
    print(i,j)
print(flat_data)
print("Flattened JSON:")
print(json.dumps(flat_data, indent=2))

   
with open("flattened_data.json", "w") as f:
    json.dump(flat_data, f, indent=2)