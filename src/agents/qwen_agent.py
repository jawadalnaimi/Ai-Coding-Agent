from typing import Dict, Any, Optional
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import os
import logging
from .base_agent import BaseAgent

class QwenAgent(BaseAgent):
    """Implementation of AI coding agent using Qwen"""
    
    def __init__(self, model_path: str, config: Dict[str, Any]):
        super().__init__(model_path, config)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.logger.info(f"Using device: {self.device}")
        
    def _load_model(self):
        """Load Qwen model."""
        try:
            self.logger.info(f"Loading Qwen model from {self.model_path}")
            
            if not os.path.exists(self.model_path):
                raise FileNotFoundError(f"Model path does not exist: {self.model_path}")
                
            # Load tokenizer and model
            tokenizer = AutoTokenizer.from_pretrained(
                self.model_path, 
                trust_remote_code=True
            )
            model = AutoModelForCausalLM.from_pretrained(
                self.model_path,
                torch_dtype=torch.float16 if self.device.type == "cuda" else torch.float32,
                low_cpu_mem_usage=True,
                device_map="auto" if self.device.type == "cuda" else None,
                trust_remote_code=True
            )
            
            model.to(self.device)
            self.logger.info("Qwen model loaded successfully")
            
            return {"model": model, "tokenizer": tokenizer}
        except Exception as e:
            self.logger.error(f"Failed to load Qwen model: {str(e)}")
            raise
    
    def generate_code(self, prompt: str, language: str, **kwargs) -> str:
        """Generate code using Qwen"""
        try:
            self.logger.info(f"Generating {language} code from prompt")
            
            # Prepare the prompt with appropriate formatting
            system_prompt = self.config.get("system_prompt", "")
            language_prompt = f"Generate {language} code for the following task:"
            full_prompt = f"{system_prompt}\n\n{language_prompt}\n\n{prompt}\n\n"
            
            # Tokenize input
            inputs = self.model["tokenizer"](full_prompt, return_tensors="pt").to(self.device)
            
            # Generate response
            with torch.no_grad():
                output = self.model["model"].generate(
                    inputs.input_ids,
                    max_new_tokens=self.config.get("max_tokens", 2048),
                    temperature=self.config.get("temperature", 0.7),
                    top_p=self.config.get("top_p", 0.95),
                    do_sample=True,
                    pad_token_id=self.model["tokenizer"].eos_token_id
                )
            
            # Decode the response
            generated_text = self.model["tokenizer"].decode(output[0], skip_special_tokens=True)
            
            # Extract just the generated code (remove the prompt)
            code = generated_text[len(full_prompt):].strip()
            
            # Format the code
            from ..utils.code_utils import format_python_code, format_cpp_code
            if language.lower() == "python":
                code = format_python_code(code, self.config)
            elif language.lower() in ["cpp", "c++"]:
                code = format_cpp_code(code, self.config)
                
            return code
        except Exception as e:
            self.logger.error(f"Code generation failed: {str(e)}")
            raise
    
    def explain_code(self, code: str, **kwargs) -> str:
        """Explain code using Qwen"""
        try:
            self.logger.info("Generating code explanation")
            
            # Prepare the prompt
            system_prompt = self.config.get("system_prompt", "")
            explanation_prompt = "Explain the following code in detail, including its purpose, functionality, and any notable patterns or techniques used:"
            full_prompt = f"{system_prompt}\n\n{explanation_prompt}\n\n```\n{code}\n```\n\n"
            
            # Tokenize input
            inputs = self.model["tokenizer"](full_prompt, return_tensors="pt").to(self.device)
            
            # Generate response
            with torch.no_grad():
                output = self.model["model"].generate(
                    inputs.input_ids,
                    max_new_tokens=self.config.get("max_tokens", 2048),
                    temperature=self.config.get("temperature", 0.7),
                    top_p=self.config.get("top_p", 0.95),
                    do_sample=True,
                    pad_token_id=self.model["tokenizer"].eos_token_id
                )
            
            # Decode the response
            generated_text = self.model["tokenizer"].decode(output[0], skip_special_tokens=True)
            
            # Extract just the explanation (remove the prompt)
            explanation = generated_text[len(full_prompt):].strip()
                
            return explanation
        except Exception as e:
            self.logger.error(f"Code explanation failed: {str(e)}")
            raise
    
    def refactor_code(self, code: str, instructions: str, **kwargs) -> str:
        """Refactor code using Qwen"""
        try:
            self.logger.info("Refactoring code")
            
            # Prepare the prompt
            system_prompt = self.config.get("system_prompt", "")
            refactor_prompt = f"Refactor the following code according to these instructions: {instructions}"
            full_prompt = f"{system_prompt}\n\n{refactor_prompt}\n\n```\n{code}\n```\n\n"
            
            # Tokenize input
            inputs = self.model["tokenizer"](full_prompt, return_tensors="pt").to(self.device)
            
            # Generate response
            with torch.no_grad():
                output = self.model["model"].generate(
                    inputs.input_ids,
                    max_new_tokens=self.config.get("max_tokens", 2048),
                    temperature=self.config.get("temperature", 0.7),
                    top_p=self.config.get("top_p", 0.95),
                    do_sample=True,
                    pad_token_id=self.model["tokenizer"].eos_token_id
                )
            
            # Decode the response
            generated_text = self.model["tokenizer"].decode(output[0], skip_special_tokens=True)
            
            # Extract just the refactored code (remove the prompt)
            from ..utils.code_utils import extract_code_blocks
            code_blocks = extract_code_blocks(generated_text[len(full_prompt):])
            
            # Get the refactored code
            language = kwargs.get("language", "")
            if language and language in code_blocks:
                refactored_code = code_blocks[language][0]
            else:
                # If language not specified or not found, use the first code block
                for lang, blocks in code_blocks.items():
                    refactored_code = blocks[0]
                    break
                else:
                    # If no code blocks found, use the entire generated text
                    refactored_code = generated_text[len(full_prompt):].strip()
            
            # Format the code
            from ..utils.code_utils import format_python_code, format_cpp_code
            if language.lower() == "python":
                refactored_code = format_python_code(refactored_code, self.config)
            elif language.lower() in ["cpp", "c++"]:
                refactored_code = format_cpp_code(refactored_code, self.config)
                
            return refactored_code
        except Exception as e:
            self.logger.error(f"Code refactoring failed: {str(e)}")
            raise
    
    def validate_code(self, code: str, language: str) -> bool:
        """Validate code syntax"""
        from ..utils.code_utils import validate_python_syntax, validate_cpp_syntax
        
        if language.lower() == "python":
            return validate_python_syntax(code)
        elif language.lower() in ["cpp", "c++"]:
            return validate_cpp_syntax(code)
        else:
            self.logger.warning(f"Validation not implemented for language: {language}")
            return True
    
    def format_code(self, code: str, language: str) -> str:
        """Format code according to language standards"""
        from ..utils.code_utils import format_python_code, format_cpp_code
        
        if language.lower() == "python":
            return format_python_code(code, self.config)
        elif language.lower() in ["cpp", "c++"]:
            return format_cpp_code(code, self.config)
        else:
            self.logger.warning(f"Formatting not implemented for language: {language}")
            return code
