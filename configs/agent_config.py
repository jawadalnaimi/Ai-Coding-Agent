"""Configuration settings for AI coding agents."""

CLAUDE_CONFIG = {
    "model_name": "claude-3.5",
    "max_tokens": 4096,
    "temperature": 0.7,
    "top_p": 0.95,
    "context_window": 100000,
    "system_prompt": """You are an AI coding assistant. Your task is to help users by:
    1. Generating high-quality, efficient code in Python and C++
    2. Explaining code functionality and implementation details
    3. Suggesting improvements and refactoring options
    4. Following best practices and coding standards
    Please ensure all generated code is well-documented and follows language-specific conventions."""
}

QWEN_CONFIG = {
    "model_name": "Qwen-7B",
    "max_tokens": 2048,
    "temperature": 0.7,
    "top_p": 0.95,
    "context_window": 32768,
    "system_prompt": """You are an AI coding assistant. Your task is to help users by:
    1. Generating high-quality, efficient code in Python and C++
    2. Explaining code functionality and implementation details
    3. Suggesting improvements and refactoring options
    4. Following best practices and coding standards
    Please ensure all generated code is well-documented and follows language-specific conventions."""
}

# Language-specific settings
PYTHON_CONFIG = {
    "formatter": "black",
    "line_length": 88,
    "target_version": "py310",
}

CPP_CONFIG = {
    "formatter": "clang-format",
    "style": "google",
    "standard": "c++17",
}

# Logging configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
    },
    "handlers": {
        "default": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.FileHandler",
            "filename": "ai_agent.log",
            "mode": "a",
        },
    },
    "loggers": {
        "": {
            "handlers": ["default", "file"],
            "level": "INFO",
            "propagate": True
        },
    },
}
