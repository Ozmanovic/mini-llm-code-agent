import os

# Check what files are in directory
def get_files_info(working_directory, directory=None):
    
        if directory == None:
            directory = os.path.join(working_directory, ".")
        absolute_og_path = os.path.abspath(working_directory)
        target_path = os.path.join(working_directory, directory)
        final_path = os.path.abspath(target_path)

        if not final_path.startswith(absolute_og_path):
            print(f"'{absolute_og_path}' \n")
            print(f"'{target_path}'")
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        
        elif not os.path.isdir(final_path):
            return f'Error: "{directory}" is not a directory'
            
        try:
            contents = os.listdir(final_path)
            empty_list = []
        
            for item_name in contents:
                item_path = os.path.join(final_path, item_name)
                empty_list.append(f"- {item_name}: file_size:{os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}")
            final_string = "\n".join(empty_list)
            return(final_string)
        except Exception as e:
            return f"An error occurred: {e}"


# Get content of files
def get_file_content(working_directory, file_path):
     
        absolute_og_path = os.path.abspath(working_directory)
        target_path = os.path.join(working_directory, file_path)
        absolute_file_path = os.path.abspath(target_path)

        if not absolute_file_path.startswith(absolute_og_path):
            print(f"'{absolute_og_path}' \n")
            print(f"'{target_path}'")
            return f'Error: Cannot list "{absolute_file_path}" as it is outside the permitted working directory'

        elif not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" is not a file'
        
        try:
            
            empty_list = []
        
            
            MAX_CHARS = 10000
            with open(absolute_file_path, "r") as f:
                content = f.read()
                if len(content) > MAX_CHARS:
                    file_content_string = content[:MAX_CHARS]
                    empty_list.append(file_content_string)
                    empty_list.append(f'[...File "{absolute_file_path}" truncated at 10000 characters]')
                else:
                     file_content_string = content
                     empty_list.append(file_content_string)
                        
                    
                
            final_string = " ".join(empty_list)
            return(final_string)
        except Exception as e:
            return f"An error occurred: {e}"
        

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
                
                

        
        


    




