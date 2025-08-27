'''Data Format Converter (CSV to JSON)
 • Concepts: File I/O, CSV and JSON modules, data transformation, and list comprehensions.
 • Description:
 Develop a script that reads data from a CSV file and converts each row into a JSON object. 
The final output should be a JSON file containing an array of these objects.
 • Validation:
 Provide a sample CSV file and confirm that the output JSON file accurately represents the 
CSV content structure.'''
import csv
import json

def csv_to_json(csv_file, json_file):
    try:
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]  

        with open(json_file, mode='w') as file:
            json.dump(data, file, indent=2)

        print(f"Successfully converted '{csv_file}' to '{json_file}'.")

    except FileNotFoundError:
        print(f"Error: '{csv_file}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")


csv_to_json("employees.csv", "employees.json")