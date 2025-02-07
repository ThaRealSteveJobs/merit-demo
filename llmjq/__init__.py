"""
LLMJQ - A tool to generate and execute jq programs using LLMs.
"""
from typing import Optional
import os
import sys
import subprocess
from dataclasses import dataclass

import typer
from openai import OpenAI
from rich import print

app = typer.Typer()

# most basic typer app:
@app.command()
def main():
    print("Hello, world!")


if __name__ == "__main__":
    app()
