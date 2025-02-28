#!/usr/bin/env python3
"""
Script to initialize and test AI models after downloading.
This script verifies that models can be loaded and used for inference.
"""

import argparse
import os
import logging
import sys
import torch
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

def test_model(model_path, model_type):
    """
    Test a downloaded model by loading it and running a simple inference.
    
    Args:
        model_path: Path to the model directory
        model_type: Type of model (claude or qwen)
    """
    logger.info(f"Testing {model_type} model at {model_path}")
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model path does not exist: {model_path}")
    
    try:
        # Determine device
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logger.info(f"Using device: {device}")
        
        # Set trust_remote_code for Qwen models
        trust_remote_code = model_type.lower() == "qwen"
        
        # Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(
            model_path, 
            trust_remote_code=trust_remote_code
        )
        
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16 if device.type == "cuda" else torch.float32,
            low_cpu_mem_usage=True,
            device_map="auto" if device.type == "cuda" else None,
            trust_remote_code=trust_remote_code
        )
        
        model.to(device)
        
        # Test with a simple prompt
        test_prompt = "Write a simple Python function to calculate the factorial of a number."
        logger.info("Running test inference with prompt: 'Write a simple Python function to calculate the factorial of a number.'")
        
        inputs = tokenizer(test_prompt, return_tensors="pt").to(device)
        
        with torch.no_grad():
            output = model.generate(
                inputs.input_ids,
                max_new_tokens=200,
                temperature=0.7,
                top_p=0.95,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        
        logger.info("Model generated response successfully")
        logger.info(f"Response preview: {generated_text[:100]}...")
        
        logger.info(f"Successfully tested {model_type} model")
        return True
        
    except Exception as e:
        logger.error(f"Error testing model: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Test AI models for local inference")
    parser.add_argument(
        "--model-type",
        choices=["claude", "qwen"],
        required=True,
        help="Type of model to test"
    )
    parser.add_argument(
        "--model-path",
        required=True,
        help="Path to the model directory"
    )
    
    args = parser.parse_args()
    
    success = test_model(args.model_path, args.model_type)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
