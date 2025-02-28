# Troubleshooting Guide

This guide addresses common issues you might encounter when setting up and using the Local AI Coding Agent.

## Installation Issues

### Package Installation Failures

**Problem**: Error installing dependencies.

**Solutions**:
- Update pip: `pip install --upgrade pip`
- Install build tools: `sudo apt install build-essential` (Ubuntu) or `xcode-select --install` (macOS)
- Try installing problematic packages individually with verbose output: `pip install <package> -v`

### CUDA/GPU Issues

**Problem**: CUDA-related errors or GPU not being detected.

**Solutions**:
- Verify CUDA installation: `nvcc --version`
- Check GPU is recognized: `nvidia-smi`
- Ensure CUDA version matches PyTorch requirements
- Install the correct PyTorch version for your CUDA: [PyTorch Installation Guide](https://pytorch.org/get-started/locally/)
- Try forcing CPU mode: `export CUDA_VISIBLE_DEVICES=""`

## Model Loading Issues

### Model Download Failures

**Problem**: Cannot download models from Hugging Face.

**Solutions**:
- Check internet connection
- Verify you have enough disk space
- Try with a VPN if regional restrictions apply
- Download manually from Hugging Face and place in the appropriate directory

### Out of Memory Errors

**Problem**: System runs out of memory when loading models.

**Solutions**:
- Use a smaller model variant
- Enable memory-efficient loading: `--low-cpu-mem-usage`
- For GPU: try using `--device-map auto` to spread across multiple GPUs
- Increase swap space on your system
- Use quantized models (4-bit or 8-bit) to reduce memory usage

## Runtime Issues

### Slow Generation

**Problem**: Code generation is very slow.

**Solutions**:
- Use a GPU if available
- Reduce the context length in configuration
- Try a smaller model
- Use quantization for faster inference
- Optimize batch size for your hardware

### Poor Quality Output

**Problem**: Generated code is low quality or contains errors.

**Solutions**:
- Try a different model
- Adjust temperature and top_p parameters
- Provide more detailed prompts
- Use the refactoring feature to improve initial output

### Python Import Errors

**Problem**: `ModuleNotFoundError` or similar import errors.

**Solutions**:
- Ensure package is installed in the current environment
- Check for path issues: `import sys; print(sys.path)`
- Verify you're using the correct Python interpreter: `which python`
- Try reinstalling the package with `-e` flag

## C++ Specific Issues

### Compiler Errors

**Problem**: C++ validation or compilation fails.

**Solutions**:
- Ensure g++ is installed: `g++ --version`
- Install missing development libraries
- Check for C++ standard compatibility issues
- Manually compile with verbose output: `g++ -v file.cpp`

## Logging and Debugging

If you encounter issues not covered here:

1. Enable debug logging:
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

2. Check log files in the project directory

3. Run with traceback for more details:
   ```bash
   python -m trace --trace main.py
   ```

## Getting Help

If you continue to experience issues:

1. Check existing GitHub issues
2. Provide detailed information when reporting new issues:
   - System specifications
   - Error messages and stack traces
   - Steps to reproduce
   - Log outputs
