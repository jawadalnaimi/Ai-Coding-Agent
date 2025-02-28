# Usage Guide

This guide explains how to use the Local AI Coding Agent for Python and C++ development.

## Basic Usage

The AI Coding Agent can be used through the command line interface (CLI) with the following basic syntax:

```bash
ai-code --agent <agent_type> --model-path <path_to_model> --language <language> <action> <input>
```

Where:
- `<agent_type>`: Either "claude" or "qwen"
- `<path_to_model>`: Path to the model directory
- `<language>`: Either "python" or "cpp"
- `<action>`: One of "generate", "explain", or "refactor"
- `<input>`: The prompt or code to process

## Example Commands

### Code Generation

Generate Python code:

```bash
ai-code --agent claude --model-path src/models/claude --language python generate "Write a function that calculates the prime factors of a number"
```

Generate C++ code:

```bash
ai-code --agent qwen --model-path src/models/qwen --language cpp generate "Create a class for a linked list with methods for insertion, deletion, and traversal"
```

### Code Explanation

Explain existing code:

```bash
ai-code --agent claude --model-path src/models/claude explain "def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)"
```

You can also provide a file path to explain:

```bash
ai-code --agent claude --model-path src/models/claude explain --file path/to/code.py
```

### Code Refactoring

Refactor code for better performance:

```bash
ai-code --agent qwen --model-path src/models/qwen refactor "int factorial(int n) {
    int result = 1;
    for(int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}"
```

With specific refactoring instructions:

```bash
ai-code --agent claude --model-path src/models/claude refactor --instructions "Optimize for performance and readability" --file path/to/code.cpp
```

## Advanced Usage

### Setting Output File

Save the generated or refactored code to a file:

```bash
ai-code --agent claude --model-path src/models/claude --language python generate "Write a function to check if a string is a palindrome" --output palindrome.py
```

### Adjusting Generation Parameters

Customize the generation parameters:

```bash
ai-code --agent qwen --model-path src/models/qwen --language cpp generate "Write a sorting algorithm" --temperature 0.8 --max-tokens 1000
```

### Batch Processing

Process multiple files:

```bash
ai-code --agent claude --model-path src/models/claude refactor --directory path/to/src --pattern "*.py" --instructions "Add docstrings and type hints"
```

## Integration with Development Environments

### Using with VSCode

1. Open the command palette (Ctrl+Shift+P)
2. Run "Terminal: Create New Integrated Terminal"
3. Use the CLI commands as described above

### Using with Jupyter Notebooks

You can use the AI Coding Agent in Jupyter notebooks by installing the package and importing it:

```python
from ai_coding_agent import ClaudeAgent

agent = ClaudeAgent("path/to/model", {})
code = agent.generate_code("Create a function to analyze text sentiment", "python")
print(code)
```

## Best Practices

1. **Be Specific**: Provide detailed prompts for better results
2. **Review Generated Code**: Always review and test generated code
3. **Iterative Refinement**: Use the refactor action to improve initial generations
4. **Provide Context**: For complex tasks, include relevant context in your prompt
5. **Use Comments**: Include comments in your code to guide the AI during refactoring

## Limitations

- The agent may not always generate perfect code on the first try
- Complex architectural decisions may require human guidance
- Performance depends on the quality and size of the model used
- The agent works best with standard libraries and common patterns

## Troubleshooting

If you encounter issues, refer to the [Troubleshooting Guide](TROUBLESHOOTING.md) for solutions to common problems.
