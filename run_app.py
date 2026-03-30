#!/usr/bin/env python3
"""
Script to run the Streamlit app
"""

import subprocess
import sys
import os

def main():
    print("🚀 Starting Personal Knowledge Base Chatbot...")
    print("=" * 50)
    
    # Check if .env file exists
    if not os.path.exists(".env"):
        print("⚠️  .env file not found!")
        print("Please run: pipenv run python setup_groq.py")
        return
    
    # Check if vector database exists
    if not os.path.exists("db"):
        print("⚠️  Vector database not found!")
        print("Please run: pipenv run python ingest.py")
        print("This will create the vector database from your PDF documents.")
        return
    
    print("✅ Environment looks good!")
    print("🌐 Starting Streamlit app...")
    print("📱 The app will open in your browser automatically")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Run streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.address", "localhost",
            "--server.port", "8501"
        ])
    except KeyboardInterrupt:
        print("\n👋 Shutting down the app...")

if __name__ == "__main__":
    main()