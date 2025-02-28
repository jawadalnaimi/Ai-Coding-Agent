# Installation Guide

This guide provides detailed instructions for setting up the Local AI Coding Agent on your system.

## Prerequisites

Before installing, ensure your system meets the following requirements:

### Hardware Requirements
- CPU: Minimum 8 cores (16 threads recommended)
- RAM: Minimum 32GB (64GB recommended)
- Storage: 500GB SSD
- GPU: NVIDIA GPU with at least 8GB VRAM (optional but recommended)

### Software Requirements
- Ubuntu 22.04 LTS or macOS 12+
- Python 3.10+
- CUDA 11.7+ and cuDNN (if using GPU)

## Step 1: Clone the Repository

```bash
git clone https://github.com/jawadalnaimi/Ai-Coding-Agent.git
cd Ai-Coding-Agent
```

## Step 2: Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install -e .
```

This will install the package in development mode with all required dependencies.

For development purposes, you can install additional tools:

```bash
pip install -e ".[dev]"
```

## Step 4: Download Models

The system requires AI models to function. You can download them using the provided script:

### For Claude Model:

```bash
python scripts/download_models.py --model-type claude --model-name anthropic/claude-3-haiku-20240307 --output-dir src/models/claude
```

### For Qwen Model:

```bash
python scripts/download_models.py --model-type qwen --model-name Qwen/Qwen-7B-Chat --output-dir src/models/qwen
```

Note: Model downloads can be large (several GB). Ensure you have sufficient disk space and a stable internet connection.

## Step 5: Test the Installation

Verify that the models are working correctly:

```bash
python scripts/initialize_models.py --model-type claude --model-path src/models/claude
python scripts/initialize_models.py --model-type qwen --model-path src/models/qwen
```

## Step 6: Run the AI Coding Agent

You can now run the AI coding agent using the command:

```bash
ai-code --agent claude --model-path src/models/claude --language python generate "Write a function to calculate the Fibonacci sequence"
```

Or for C++ code:

```bash
ai-code --agent qwen --model-path src/models/qwen --language cpp generate "Write a class for a binary search tree"
```

## Troubleshooting

### Common Issues:

1. **Out of Memory Errors**: 
   - Try using a smaller model
   - Reduce batch size or context length in the configuration

2. **CUDA/GPU Issues**:
   - Ensure CUDA is properly installed
   - Update GPU drivers
   - Try running on CPU with `--device cpu`

3. **Import Errors**:
   - Ensure all dependencies are installed
   - Check for version conflicts

For more detailed troubleshooting, refer to the [Troubleshooting Guide](TROUBLESHOOTING.md).
