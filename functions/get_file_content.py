import os

# Function for LLM to be able to read files. With max CHARS of file set at 10000 chars.
def get_file_content(working_directory, file_path):
     
        absolute_og_path = os.path.abspath(working_directory)
        target_path = os.path.join(working_directory, file_path)
        absolute_file_path = os.path.abspath(target_path)

        if not absolute_file_path.startswith(absolute_og_path):
            print(f"'{absolute_og_path}' \n")
            print(f"'{target_path}'")
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

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