#!/usr/bin/env python3
"""
Script to help set up Groq API key for OpenAI-compatible interface
"""

import os
from pathlib import Path

def setup_groq_api_key():
    print("Groq API Key Setup")
    print("=" * 50)
    
    api_key = input("Please enter your Groq API key: ").strip()
    
    if not api_key:
        print("No API key provided. Exiting.")
        return
    
    env_file = Path(".env")
    
    if env_file.exists():
        # Read existing content
        with open(env_file, 'r') as f:
            content = f.read()
        
        # Replace or add GROQ_API_KEY
        lines = content.split('\n')
        updated = False
        
        for i, line in enumerate(lines):
            if line.startswith('GROQ_API_KEY='):
                lines[i] = f'GROQ_API_KEY={api_key}'
                updated = True
                break
        
        if not updated:
            lines.append(f'GROQ_API_KEY={api_key}')
        
        # Write back
        with open(env_file, 'w') as f:
            f.write('\n'.join(lines))
    else:
        # Create new .env file
        with open(env_file, 'w') as f:
            f.write(f'GROQ_API_KEY={api_key}\n')
    
    print(f"✅ API key saved to {env_file}")
    print("\nYou can now run your chatbot with:")
    print("pipenv run python chat.py")

if __name__ == "__main__":
    setup_groq_api_key()