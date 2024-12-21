"""Utility functions for code generation and manipulation."""

import subprocess
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

def format_python_code(code: str, config: Dict[str, Any]) -> str:
    """
    Format Python code using black.
    
    Args:
        code: Python code to format
        config: Formatting configuration
        
    Returns:
        Formatted code
    """
    try:
        import black
        mode = black.FileMode(
            line_length=config.get("line_length", 88),
            target_versions={black.TargetVersion[config.get("target_version", "py310")]}
        )
        return black.format_str(code, mode=mode)
    except Exception as e:
        logger.error(f"Failed to format Python code: {str(e)}")
        return code

def format_cpp_code(code: str, config: Dict[str, Any]) -> str:
    """
    Format C++ code using clang-format.
    
    Args:
        code: C++ code to format
        config: Formatting configuration
        
    Returns:
        Formatted code
    """
    try:
        cmd = ["clang-format", f"-style={config.get('style', 'google')}"]
        process = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        formatted_code, stderr = process.communicate(input=code)
        if process.returncode != 0:
            logger.error(f"clang-format failed: {stderr}")
            return code
        return formatted_code
    except Exception as e:
        logger.error(f"Failed to format C++ code: {str(e)}")
        return code

def validate_python_syntax(code: str) -> bool:
    """
    Validate Python code syntax.
    
    Args:
        code: Python code to validate
        
    Returns:
        True if syntax is valid, False otherwise
    """
    try:
        compile(code, "<string>", "exec")
        return True
    except SyntaxError:
        return False

def validate_cpp_syntax(code: str, compiler: str = "g++") -> bool:
    """
    Validate C++ code syntax using compiler.
    
    Args:
        code: C++ code to validate
        compiler: C++ compiler to use
        
    Returns:
        True if syntax is valid, False otherwise
    """
    try:
        with open("temp.cpp", "w") as f:
            f.write(code)
        
        process = subprocess.run(
            [compiler, "-fsyntax-only", "temp.cpp"],
            capture_output=True,
            text=True
        )
        return process.returncode == 0
    except Exception:
        return False
    finally:
        try:
            import os
            os.remove("temp.cpp")
        except:
            pass

def extract_code_blocks(text: str) -> Dict[str, str]:
    """
    Extract code blocks from markdown-style text.
    
    Args:
        text: Text containing code blocks
        
    Returns:
        Dictionary mapping language to code blocks
    """
    import re
    
    code_blocks = {}
    pattern = r"```(\w+)\n(.*?)```"
    matches = re.finditer(pattern, text, re.DOTALL)
    
    for match in matches:
        language = match.group(1).lower()
        code = match.group(2).strip()
        if language in code_blocks:
            code_blocks[language].append(code)
        else:
            code_blocks[language] = [code]
    
    return code_blocks

def get_language_from_file(filename: str) -> Optional[str]:
    """
    Determine programming language from file extension.
    
    Args:
        filename: Name of the file
        
    Returns:
        Language name or None if unknown
    """
    extension_map = {
        ".py": "python",
        ".cpp": "cpp",
        ".hpp": "cpp",
        ".h": "cpp",
        ".c": "c",
    }
    
    import os
    _, ext = os.path.splitext(filename)
    return extension_map.get(ext.lower())
