"""
Tests for AI coding agents.
"""

import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agents.base_agent import BaseAgent
from src.agents.claude_agent import ClaudeAgent
from src.agents.qwen_agent import QwenAgent


class TestBaseAgent(unittest.TestCase):
    """Tests for the BaseAgent class."""
    
    def test_abstract_methods(self):
        """Test that BaseAgent cannot be instantiated directly."""
        with self.assertRaises(TypeError):
            BaseAgent("model_path", {})


class TestClaudeAgent(unittest.TestCase):
    """Tests for the ClaudeAgent class."""
    
    @patch('src.agents.claude_agent.AutoModelForCausalLM')
    @patch('src.agents.claude_agent.AutoTokenizer')
    @patch('os.path.exists', return_value=True)
    def test_initialization(self, mock_exists, mock_tokenizer, mock_model):
        """Test that ClaudeAgent can be initialized."""
        # Setup mocks
        mock_tokenizer.from_pretrained.return_value = MagicMock()
        mock_model.from_pretrained.return_value = MagicMock()
        
        # Initialize agent
        agent = ClaudeAgent("dummy_path", {})
        
        # Assert model path was checked
        mock_exists.assert_called_once_with("dummy_path")
        
        # Assert tokenizer and model were loaded
        mock_tokenizer.from_pretrained.assert_called_once()
        mock_model.from_pretrained.assert_called_once()
    
    @patch('src.agents.claude_agent.AutoModelForCausalLM')
    @patch('src.agents.claude_agent.AutoTokenizer')
    @patch('os.path.exists', return_value=True)
    def test_generate_code(self, mock_exists, mock_tokenizer, mock_model):
        """Test code generation."""
        # Setup mocks
        tokenizer_mock = MagicMock()
        model_mock = MagicMock()
        
        tokenizer_mock.return_value = MagicMock()
        tokenizer_mock.decode.return_value = "System prompt\n\nLanguage prompt\n\nUser prompt\n\n# Generated Python code"
        
        model_mock.generate.return_value = [MagicMock()]
        
        mock_tokenizer.from_pretrained.return_value = tokenizer_mock
        mock_model.from_pretrained.return_value = model_mock
        
        # Initialize agent
        agent = ClaudeAgent("dummy_path", {"system_prompt": "System prompt"})
        agent.model = {"model": model_mock, "tokenizer": tokenizer_mock}
        
        # Generate code
        result = agent.generate_code("User prompt", "python")
        
        # Assert result
        self.assertEqual(result, "# Generated Python code")


class TestQwenAgent(unittest.TestCase):
    """Tests for the QwenAgent class."""
    
    @patch('src.agents.qwen_agent.AutoModelForCausalLM')
    @patch('src.agents.qwen_agent.AutoTokenizer')
    @patch('os.path.exists', return_value=True)
    def test_initialization(self, mock_exists, mock_tokenizer, mock_model):
        """Test that QwenAgent can be initialized."""
        # Setup mocks
        mock_tokenizer.from_pretrained.return_value = MagicMock()
        mock_model.from_pretrained.return_value = MagicMock()
        
        # Initialize agent
        agent = QwenAgent("dummy_path", {})
        
        # Assert model path was checked
        mock_exists.assert_called_once_with("dummy_path")
        
        # Assert tokenizer and model were loaded
        mock_tokenizer.from_pretrained.assert_called_once()
        mock_model.from_pretrained.assert_called_once()
    
    @patch('src.agents.qwen_agent.AutoModelForCausalLM')
    @patch('src.agents.qwen_agent.AutoTokenizer')
    @patch('os.path.exists', return_value=True)
    def test_generate_code(self, mock_exists, mock_tokenizer, mock_model):
        """Test code generation."""
        # Setup mocks
        tokenizer_mock = MagicMock()
        model_mock = MagicMock()
        
        tokenizer_mock.return_value = MagicMock()
        tokenizer_mock.decode.return_value = "System prompt\n\nLanguage prompt\n\nUser prompt\n\n// Generated C++ code"
        
        model_mock.generate.return_value = [MagicMock()]
        
        mock_tokenizer.from_pretrained.return_value = tokenizer_mock
        mock_model.from_pretrained.return_value = model_mock
        
        # Initialize agent
        agent = QwenAgent("dummy_path", {"system_prompt": "System prompt"})
        agent.model = {"model": model_mock, "tokenizer": tokenizer_mock}
        
        # Generate code
        result = agent.generate_code("User prompt", "cpp")
        
        # Assert result
        self.assertEqual(result, "// Generated C++ code")


if __name__ == '__main__':
    unittest.main()
