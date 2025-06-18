import os

# Function for the llm to write in a file
def write_file(working_directory, file_path, content):
     
        absolute_og_path = os.path.abspath(working_directory)
        target_path = os.path.join(working_directory, file_path)
        absolute_file_path = os.path.abspath(target_path)

        if not absolute_file_path.startswith(absolute_og_path):
            print(f"'{absolute_og_path}' \n")
            print(f"'{target_path}'")
            return f'Error: Cannot list "{absolute_file_path}" as it is outside the permitted working directory'
        try:
             
            if not os.path.exists(absolute_file_path):
                directory = os.path.dirname(absolute_file_path) 
                os.makedirs(directory, exist_ok=True)
                with open(absolute_file_path, 'w') as f:
                    f.write(content)
                    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            else:
                with open(absolute_file_path, 'w') as f:
                    f.write(content)
                    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f"Error: {e}"
                