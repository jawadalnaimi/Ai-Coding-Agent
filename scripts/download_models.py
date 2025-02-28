#!/usr/bin/env python3
"""
Script to download and prepare AI models for local inference.
This script handles downloading models from Hugging Face and preparing them for local use.
"""

import argparse
import os
import logging
import sys
from huggingface_hub import snapshot_download
from transformers import AutoTokenizer, AutoModelForCausalLM

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def download_model(model_name, output_dir, model_type):
    """
    Download a model from Hugging Face Hub.
    
    Args:
        model_name: Name of the model on Hugging Face Hub
        output_dir: Directory to save the model
        model_type: Type of model (claude or qwen)
    """
    logger.info(f"Downloading {model_type} model: {model_name}")
    
    # Create the output directory
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Download the model files
        snapshot_download(
            repo_id=model_name,
            local_dir=output_dir,
            local_dir_use_symlinks=False,
            ignore_patterns=["*.h5", "*.ot", "*.msgpack"]  # Ignore large unnecessary files
        )
        
        logger.info(f"Model files downloaded to {output_dir}")
        
        # Load and save the model and tokenizer to ensure they work
        logger.info("Verifying model and tokenizer...")
        
        trust_remote_code = model_type.lower() == "qwen"
        
        tokenizer = AutoTokenizer.from_pretrained(
            output_dir, 
            trust_remote_code=trust_remote_code
        )
        model = AutoModelForCausalLM.from_pretrained(
            output_dir,
            low_cpu_mem_usage=True,
            trust_remote_code=trust_remote_code
        )
        
        # Save the model and tokenizer
        tokenizer.save_pretrained(output_dir)
        model.save_pretrained(output_dir)
        
        logger.info(f"Successfully downloaded and verified {model_type} model")
        
    except Exception as e:
        logger.error(f"Error downloading model: {str(e)}")
        raise

def main():
    parser = argparse.ArgumentParser(description="Download AI models for local inference")
    parser.add_argument(
        "--model-type",
        choices=["claude", "qwen"],
        required=True,
        help="Type of model to download"
    )
    parser.add_argument(
        "--model-name",
        required=True,
        help="Name of the model on Hugging Face Hub"
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory to save the model"
    )
    
    args = parser.parse_args()
    
    try:
        download_model(args.model_name, args.output_dir, args.model_type)
    except Exception as e:
        logger.error(f"Failed to download model: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
