import os


def get_files_info(working_directory, directory=None):
    
        if directory == None:
            directory = os.path.join(working_directory, ".")
        absolute_og_path = os.path.abspath(working_directory)
        target_path = os.path.join(working_directory, directory)
        final_path = os.path.abspath(target_path)

        if not final_path.startswith(absolute_og_path):
            print(f"'{absolute_og_path}' \n")
            print(f"'{target_path}'")
            print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

        
        elif not os.path.isdir(final_path):
            print(f'Error: "{directory}" is not a directory')
            return
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



def get_file_content(working_directory, file_path):
     
         
        if file_path == None:
            directory = os.path.join(working_directory, ".")
        absolute_og_path = os.path.abspath(working_directory)
        target_path = os.path.join(working_directory, file_path)
        final_path = os.path.abspath(target_path)

        if not final_path.startswith(absolute_og_path):
            print(f"'{absolute_og_path}' \n")
            print(f"'{target_path}'")
            print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

        elif not os.path.isfile(final_path):
            print(f'Error: "{file_path}" is not a file')
            return    

        
        


    




#tests        
direct = "calculator"
working_directory = f"/home/ozmanovic/workspace/github.com/Ozmanovic/mini-llm-code-agent/{direct}"
directory = "pkg"
get_files_info(working_directory, directory)