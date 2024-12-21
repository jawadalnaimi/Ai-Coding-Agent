from setuptools import setup, find_packages

setup(
    name="ai-coding-agent",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "accelerate>=0.20.0",
        "bitsandbytes>=0.39.0",
        "sentencepiece>=0.1.99",
        "protobuf>=4.23.3",
        "scipy>=1.11.1",
        "numpy>=1.24.3",
        "tqdm>=4.65.0",
        "psutil>=5.9.5",
        "packaging>=23.1",
        "huggingface_hub>=0.15.1",
        "einops>=0.6.1",
        "colorama>=0.4.6",
        "rich>=13.4.2",
    ],
    extras_require={
        "dev": [
            "black",
            "pylint",
            "pytest",
            "pytest-cov",
        ]
    },
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "ai-code=src.main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="Local AI coding agent using Claude 3.5 and Qwen models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ai-coding-agent",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
