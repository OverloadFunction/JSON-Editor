import json
import os

print('''
             _  _____  ____  _   _        
            | |/ ____|/ __ \| \ | |       
            | | (___ | |  | |  \| |       
        _   | |\___ \| |  | | . ` |       
       | |__| |____) | |__| | |\  |       
  ______\____/|_____/_\____/|_|_\_|_____  
 |  ____|  __ \_   _|__   __/ __ \|  __ \ 
 | |__  | |  | || |    | | | |  | | |__) |
 |  __| | |  | || |    | | | |  | |  _  / 
 | |____| |__| || |_   | | | |__| | | \ \ 
 |______|_____/_____|  |_|  \____/|_|  \_\
                                          
                                                                              
''')

print("------ Developed by uj4 | https://uj4.dev/ ------")
print("")

data_folder = 'Data'
output_directory = 'Output'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

json_files = [f for f in os.listdir(data_folder) if f.endswith('.json')]

if not json_files:
    print("Unable to locate json files, please put your files in the Data folder...")
    print("Make sure they end with .json | e.g. data.json")
    exit()
else:
    print("Located the following json files:")
    for idx, file_name in enumerate(json_files, start=1):
        print(f"{idx}. {file_name}")
    
    while True:
        try:
            file_index = int(input("Please enter the number of the JSON file to process: ")) - 1
            if file_index < 0 or file_index >= len(json_files):
                raise ValueError("Invalid file index | Please enter a valid number.")
            break
        except ValueError as e:
            print(e)
    
    selected_file = os.path.join(data_folder, json_files[file_index])
    output_file_path = os.path.join(output_directory, json_files[file_index])

    field_name = input("Enter the name of the field to update: ").strip()

    new_value = input("Enter the new value for the field: ").strip()
    

    def update_json_field(input_file_path, field_name, new_value, output_file_path):
            try:
                # Read the existing JSON data
                with open(input_file_path, 'r') as file:
                    data = json.load(file)
                
                # Check if data is a list of dictionaries
                if not isinstance(data, list) or not all(isinstance(entry, dict) for entry in data):
                    raise ValueError("JSON file should contain a list of dictionaries.")
                
                # Update the specified field
                for entry in data:
                    if field_name in entry:
                        entry[field_name] = new_value

                # Write the updated data to a new file
                with open(output_file_path, 'w') as file:
                    json.dump(data, file, indent=4)
                
                print(f"Successfully updated '{field_name}' to '{new_value}' in {output_file_path}")
            
            except FileNotFoundError:
                print(f"Error: The file '{input_file_path}' does not exist.")
            except json.JSONDecodeError:
                print("Error: Failed to decode JSON. Ensure the file contains valid JSON.")
            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    update_json_field(selected_file, field_name, new_value, output_file_path)
