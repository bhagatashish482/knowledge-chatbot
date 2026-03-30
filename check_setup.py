#!/usr/bin/env python3
"""
Check if the setup is ready for the Streamlit app
"""

import os
from pathlib import Path

def check_setup():
    print("🔍 Checking setup...")
    print("=" * 50)
    
    issues = []
    
    # Check .env file
    if not os.path.exists(".env"):
        issues.append("❌ .env file not found")
        print("❌ .env file not found")
        print("   Run: pipenv run python setup_groq.py")
    else:
        print("✅ .env file exists")
        
        # Check API key
        from dotenv import load_dotenv
        load_dotenv()
        if not os.getenv("GROQ_API_KEY"):
            issues.append("❌ GROQ_API_KEY not set in .env")
            print("❌ GROQ_API_KEY not set in .env")
        else:
            print("✅ GROQ_API_KEY is set")
    
    # Check data directory
    data_dir = Path("data")
    if not data_dir.exists():
        issues.append("❌ data/ directory not found")
        print("❌ data/ directory not found")
        print("   Create it and add your PDF files")
    else:
        pdf_files = list(data_dir.glob("*.pdf"))
        if not pdf_files:
            issues.append("❌ No PDF files in data/ directory")
            print("❌ No PDF files in data/ directory")
            print("   Add some PDF files to process")
        else:
            print(f"✅ Found {len(pdf_files)} PDF file(s) in data/")
    
    # Check vector database
    if not os.path.exists("db"):
        issues.append("❌ Vector database not found")
        print("❌ Vector database not found")
        print("   Run: pipenv run python ingest.py")
    else:
        print("✅ Vector database exists")
    
    # Check imports
    try:
        import streamlit
        from rag_chain import load_qa_chain
        print("✅ All required packages imported successfully")
    except ImportError as e:
        issues.append(f"❌ Import error: {e}")
        print(f"❌ Import error: {e}")
    
    print("\n" + "=" * 50)
    
    if not issues:
        print("🎉 Everything looks good! You can run the app:")
        print("   pipenv run python run_app.py")
        print("   or")
        print("   pipenv run streamlit run app.py")
    else:
        print("⚠️  Please fix the following issues:")
        for issue in issues:
            print(f"   {issue}")
    
    return len(issues) == 0

if __name__ == "__main__":
    check_setup()