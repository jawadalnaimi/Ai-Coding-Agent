"""Main entry point for the AI coding agent."""

import argparse
import logging
import logging.config
import sys
from typing import Optional

from agents.claude_agent import ClaudeAgent
from agents.qwen_agent import QwenAgent
from configs.agent_config import (
    CLAUDE_CONFIG,
    QWEN_CONFIG,
    LOGGING_CONFIG,
    PYTHON_CONFIG,
    CPP_CONFIG,
)

# Configure logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

def create_agent(agent_type: str, model_path: str):
    """Create an AI coding agent instance."""
    if agent_type.lower() == "claude":
        return ClaudeAgent(model_path, CLAUDE_CONFIG)
    elif agent_type.lower() == "qwen":
        return QwenAgent(model_path, QWEN_CONFIG)
    else:
        raise ValueError(f"Unknown agent type: {agent_type}")

def main():
    parser = argparse.ArgumentParser(description="AI Coding Agent CLI")
    parser.add_argument(
        "--agent",
        choices=["claude", "qwen"],
        default="claude",
        help="Type of AI agent to use"
    )
    parser.add_argument(
        "--model-path",
        required=True,
        help="Path to the model weights"
    )
    parser.add_argument(
        "--language",
        choices=["python", "cpp"],
        required=True,
        help="Target programming language"
    )
    parser.add_argument(
        "action",
        choices=["generate", "explain", "refactor"],
        help="Action to perform"
    )
    parser.add_argument(
        "input",
        help="Input text (prompt for generation, code for explanation/refactoring)"
    )
    
    args = parser.parse_args()
    
    try:
        # Create AI agent
        agent = create_agent(args.agent, args.model_path)
        logger.info(f"Created {args.agent} agent successfully")
        
        # Perform requested action
        if args.action == "generate":
            result = agent.generate_code(args.input, args.language)
            print("\nGenerated Code:")
            print("=" * 80)
            print(result)
        
        elif args.action == "explain":
            result = agent.explain_code(args.input)
            print("\nCode Explanation:")
            print("=" * 80)
            print(result)
        
        elif args.action == "refactor":
            result = agent.refactor_code(args.input, "Improve code quality and efficiency")
            print("\nRefactored Code:")
            print("=" * 80)
            print(result)
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
