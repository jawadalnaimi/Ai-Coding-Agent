# Local AI Coding Agent

This project provides a complete implementation of a local AI coding agent using Claude 3.5 and Qwen models for Python and C++ development. The system is designed to run completely offline without requiring internet connectivity.

## Features

- **Fully Offline Operation**: Run the entire system locally without internet dependency
- **Multiple Model Support**: Use either Claude 3.5 or Qwen models based on your needs
- **Multi-Language Support**: Generate and analyze both Python and C++ code
- **Code Generation**: Create new code from natural language descriptions
- **Code Explanation**: Get detailed explanations of existing code
- **Code Refactoring**: Improve and optimize your existing codebase

## Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jawadalnaimi/Ai-Coding-Agent.git
   cd Ai-Coding-Agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -e .
   ```

3. **Download models**:
   ```bash
   python scripts/download_models.py --model-type claude --model-name anthropic/claude-3-haiku-20240307 --output-dir src/models/claude
   ```
   
   Or for Qwen:
   ```bash
   python scripts/download_models.py --model-type qwen --model-name Qwen/Qwen-7B-Chat --output-dir src/models/qwen
   ```

4. **Generate code**:
   ```bash
   ai-code --agent claude --model-path src/models/claude --language python generate "Write a function to calculate the factorial of a number"
   ```

For detailed installation and usage instructions, see the [Installation Guide](docs/INSTALLATION.md) and [Usage Guide](docs/USAGE.md).

## System Requirements

### Hardware Requirements
- CPU: Minimum 8 cores (16 threads recommended)
- RAM: Minimum 32GB (64GB recommended)
- Storage: 500GB SSD
- GPU: NVIDIA GPU with at least 8GB VRAM (optional but recommended)

### Software Requirements
- Ubuntu 22.04 LTS or macOS 12+
- Python 3.10+
- CUDA 11.7+ and cuDNN (if using GPU)

## Project Structure

```
ai-coding-agent/
├── configs/              # Configuration files
├── docs/                 # Documentation
├── scripts/              # Utility scripts
├── src/                  # Source code
│   ├── agents/           # Agent implementations
│   ├── models/           # Model directories
│   └── utils/            # Utility functions
├── tests/                # Test suite
├── setup.py              # Package setup
└── requirements.txt      # Dependencies
```

## Documentation

- [Installation Guide](docs/INSTALLATION.md): Detailed setup instructions
- [Usage Guide](docs/USAGE.md): How to use the AI coding agent
- [Troubleshooting](docs/TROUBLESHOOTING.md): Solutions to common issues

## How It Works

The AI Coding Agent uses large language models (LLMs) to understand and generate code. The system:

1. Loads the selected model (Claude 3.5 or Qwen) into memory
2. Processes your input request (generate, explain, or refactor)
3. Formats the input with appropriate prompts
4. Runs inference on the model
5. Post-processes the output for clean, usable code

All operations happen locally on your machine, ensuring privacy and offline functionality.

## Development Roadmap

- [ ] Add web-based UI interface
- [ ] Support for additional programming languages
- [ ] Integration with popular IDEs (VSCode, JetBrains)
- [ ] Improved code analysis capabilities
- [ ] Fine-tuning options for specialized domains

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for model hosting and libraries
- [PyTorch](https://pytorch.org/) for the deep learning framework
- [Transformers](https://github.com/huggingface/transformers) library for model implementations
