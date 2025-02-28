# Claude Model Directory

This directory is where the Claude model files will be stored after downloading.

## How to Download

Use the provided script to download the model:

```bash
python scripts/download_models.py --model-type claude --model-name <model-name> --output-dir src/models/claude
```

Replace `<model-name>` with the appropriate Hugging Face model name.

## Recommended Models

For Claude-like capabilities, you can use models such as:
- anthropic/claude-3-haiku-20240307
- anthropic/claude-3-opus-20240229
- anthropic/claude-3-sonnet-20240229

Or other compatible models available on Hugging Face.
