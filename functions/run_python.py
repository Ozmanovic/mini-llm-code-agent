import os
import subprocess


#function for LLM to be able to run python files.
def run_python_file(working_directory, file_path):

        absolute_og_path = os.path.abspath(working_directory)
        target_path = os.path.join(working_directory, file_path)
        absolute_file_path = os.path.abspath(target_path)

        if not absolute_file_path.startswith(absolute_og_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        

        elif not os.path.isfile(absolute_file_path):
            return f'Error: File "{file_path}" not found'
        
        if not os.path.exists(absolute_file_path):
           return f'Error: File "{file_path}" not found.'  
        
        elif os.path.exists(absolute_file_path) and (not absolute_file_path.endswith(".py")):
                  return f'Error: "{file_path}" is not a Python file.'
        
        try:
            result = subprocess.run(['python', file_path], cwd=working_directory, timeout=30, capture_output=True, text=True)

            
            if (result.stdout == "" or result.stdout == None) and (result.stderr == "" or result.stderr == None):
                return "No output produced"
            
            result.stdout = f"STDOUT: {result.stdout}"
            result.stderr = f"STDERR: {result.stderr}"
            if result.returncode != 0:
                retcode = f"Process exited with code {result.returncode}"
                return f"{result.stdout} {result.stderr} {retcode}"
            else:
                return f"{result.stdout} {result.stderr}"

        except Exception as e:
            return f"Error: executing Python file: {e}"
