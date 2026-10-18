from pathlib import Path

from setuptools import find_packages, setup

README = Path(__file__).parent / "README.md"

setup(
    name="pyutility",
    version="0.1.0",
    description="A reusable Python utility library",
    long_description=README.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="Prajakta Joshi",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[],
)
