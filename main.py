import os 
from dotenv import load_dotenv
from google import genai
import sys
import argparse
from google.genai import types



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

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

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






