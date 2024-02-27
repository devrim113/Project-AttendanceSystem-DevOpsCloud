# conftest.py
import os
import sys

# Get the directory containing this file (tests/), then go up one level to project_root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lambda_functions_path = os.path.join(project_root, 'lambda_functions')

# Add the 'lambda_functions' directory to sys.path
if lambda_functions_path not in sys.path:
    sys.path.insert(0, lambda_functions_path)
