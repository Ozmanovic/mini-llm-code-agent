import os 
from dotenv import load_dotenv
from google import genai
import sys
import argparse
from google.genai import types


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

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


  
        
response = client.models.generate_content(
    
    model='gemini-2.0-flash-001',
    contents =messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt) 
)
#check for --verbose
if args.verbose:
    
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if  response.function_calls == "" or response.function_calls == None: 
        print(response.text)
    else:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
else:
    if  response.function_calls == "" or response.function_calls == None: 
        print(response.text)
    else:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")






