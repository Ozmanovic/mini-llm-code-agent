# Mini LLM Code Agent

A toy implementation of an AI code agent for educational purposes. This project demonstrates basic concepts of how AI agents can interact with codebases, read files, make modifications, and execute code.

## ⚠️ SECURITY WARNING

**This is a toy implementation for learning purposes only.**

- **NOT PRODUCTION-READY**: This code agent is not secure or robust enough for real-world use
- **EDUCATIONAL ONLY**: Designed for learning about AI agent concepts, not for actual development work
- **USE WITH CAUTION**: Be very careful about what code and system access you provide to this agent
- **DO NOT SHARE**: This implementation should not be shared with others for actual use
- **LIMITED SCOPE**: Even professional AI coding tools like Cursor, Zed's Agentic Mode, and Claude Code have security limitations and require careful consideration

**Always review any code changes made by the agent before executing them.**

## Project Structure

This repository includes a simple calculator application that serves as a test project for the AI agent to interact with.

```
mini-llm-code-agent/
├── calculator/
│   ├── main.py          # CLI calculator application
│   ├── tests.py         # Unit tests
│   └── pkg/
│       ├── calculator.py # Calculator logic
│       └── render.py     # Output formatting
├── main.py              # AI agent entry point
├── requirements.txt     # Python dependencies
└── README.md
```

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Testing the Calculator Project

The calculator serves as a test project for the AI agent. To verify it works:

1. Navigate to the calculator directory:

   ```bash
   cd calculator
   ```

2. Run the tests:

   ```bash
   python3 tests.py
   ```

3. Try the calculator:
   ```bash
   python3 main.py "3 + 5"
   ```

### Running the AI Agent

From the project root:

```bash
python3 main.py
```

#### Basic Usage Examples

Run the agent with a simple prompt:

```bash
python3 main.py "hello"
```

Use verbose mode to see detailed output:

```bash
python3 main.py "hello" --verbose
```

Example prompts to try with the agent:

```bash
# Ask the agent to analyze the calculator code
python3 main.py "analyze the calculator code structure"

# Request code modifications
python3 main.py "add a modulo operator to the calculator" --verbose

# Ask for help with testing
python3 main.py "run the calculator tests and show me the results"

# General coding assistance
python3 main.py "explain how the calculator evaluation works"
```

#### Command Line Options

- `--verbose`: Enable detailed logging and output
- `--help`: Show available options and usage information

## Learning Objectives

This project helps understand:

- How AI agents can parse and understand code structure
- Basic file system operations for code modification
- Simple test execution and validation
- The challenges and limitations of automated code generation

## Limitations

- Limited code understanding capabilities
- No advanced security measures
- Simplified agent architecture
- Educational scope only

## Contributing

This is an educational project. Feel free to experiment and learn, but remember the security warnings above when making any modifications.
