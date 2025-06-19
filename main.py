import os 
from dotenv import load_dotenv
from google import genai
import sys
import argparse
from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# FUNCTION DECLARATIONS
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads contents of file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to be read, relative to the working directory.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to be run, relative to the working directory.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes in file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to be written in, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written in the file.",
            ),
        },

    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info, schema_write_file, schema_run_python_file, schema_get_file_content
    ]
)

#System prompt handling behaviour of LLM model
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

# modified the argparse so that I can get a sys.exit(1) instead of sys.exit(2) -- Need sys.exit(1) to pass the boot.dev tests =D
class modified_arg_parser(argparse.ArgumentParser):
    def __init__(self, description=None, **kwargs):
        
        super().__init__(description=description)

        
    def error(self, message):
        print(message)
        sys.exit(1)


#using argparser instead of just sys.arg because if offers more robust error handling, automatic help messages, and advanced features for building command-line interfaces, unlike manual sys.argv parsing 

parser = modified_arg_parser(description=" Mini LLM code agent. Run with 'python main.py <prompt>' ")
parser.add_argument("prompt", help="The order that you, the Meat Captain, give to your Metal Slave", nargs='+')
parser.add_argument("--verbose", "-v", action='store_true')
args = parser.parse_args()

#argparser receives the users prompts in a list e.g "Hello World --> ['Hello', 'World']" so used .join to have the prompt as a string.
user_prompt = " ".join(args.prompt)
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

# mapping functions in a dictionary so that the LLM knows what function to call based on the name.

mapping_functions = {
    
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file
}

def call_function(function_call_part, verbose=False):
        
       

        if verbose==True:

            print(f"Calling function: {function_call_part.name}({function_call_part.args})") 
        else:
            print(f" - Calling function: {function_call_part.name}")
        if function_call_part.name in mapping_functions:

            found_function = mapping_functions[function_call_part.name]
            complete_args = function_call_part.args.copy()
            complete_args["working_directory"] = "calculator"

            # Then call the function
            function_result = found_function(**complete_args)

            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"result": function_result},
                    )
                ],
            )
        else:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"Unknown function: {function_call_part.name}"},
                    )
                ],
            )
  
        
response = client.models.generate_content(
    
    model='gemini-2.0-flash-001',
    contents =messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    
)

# function call handling + iterative feedback
if args.verbose:
        
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
for i in range(20):
    if response.function_calls:
        for candidate in response.candidates:
            messages.append(candidate.content)
        
        for function_call_part in response.function_calls:
            result = call_function(function_call_part, verbose=args.verbose)
            messages.append(result)
            try:
                response_data = result.parts[0].function_response.response

                
            except (AttributeError, IndexError):
                    raise Exception("FATAL ERROR: types.content that is returned from call_function does not have '.parts[0].function_response.response' ")
            if response_data and args.verbose:
                print(f"-> {response_data}")


        
        response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
        )

    else:
        print(response.text)
        break
    



# Loop for LLM feedback iterations set at max 20. Will only iterate if a function was called.
i = 20
while i != 0:
    if response.function_calls:
        for responses in response.candidates:
            messages.append(responses.content)
            i -= 1
    else:
        print(response.text)
        break
             







