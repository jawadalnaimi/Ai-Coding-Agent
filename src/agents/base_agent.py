from abc import ABC, abstractmethod
from typing import Dict, Optional, Any
import logging

class BaseAgent(ABC):
    """Base class for AI coding agents."""
    
    def __init__(self, model_path: str, config: Dict[str, Any]):
        """
        Initialize the base agent.
        
        Args:
            model_path: Path to the model weights
            config: Configuration dictionary for the agent
        """
        self.model_path = model_path
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        
        # Initialize the model
        self.model = self._load_model()
        
    @abstractmethod
    def _load_model(self):
        """Load the AI model."""
        pass
    
    @abstractmethod
    def generate_code(self, prompt: str, language: str, **kwargs) -> str:
        """
        Generate code based on the prompt.
        
        Args:
            prompt: User's code generation prompt
            language: Target programming language
            **kwargs: Additional generation parameters
            
        Returns:
            Generated code as string
        """
        pass
    
    @abstractmethod
    def explain_code(self, code: str, **kwargs) -> str:
        """
        Explain the given code.
        
        Args:
            code: Code to explain
            **kwargs: Additional parameters
            
        Returns:
            Explanation as string
        """
        pass
    
    @abstractmethod
    def refactor_code(self, code: str, instructions: str, **kwargs) -> str:
        """
        Refactor the given code according to instructions.
        
        Args:
            code: Code to refactor
            instructions: Refactoring instructions
            **kwargs: Additional parameters
            
        Returns:
            Refactored code as string
        """
        pass
    
    def validate_code(self, code: str, language: str) -> bool:
        """
        Validate the syntax of generated code.
        
        Args:
            code: Code to validate
            language: Programming language
            
        Returns:
            True if code is valid, False otherwise
        """
        # Implementation will depend on the language
        raise NotImplementedError
    
    def format_code(self, code: str, language: str) -> str:
        """
        Format the code according to language standards.
        
        Args:
            code: Code to format
            language: Programming language
            
        Returns:
            Formatted code
        """
        # Implementation will depend on the language
        raise NotImplementedError
    
    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the loaded model.
        
        Returns:
            Dictionary containing model information
        """
        return {
            "model_path": self.model_path,
            "config": self.config
        }
