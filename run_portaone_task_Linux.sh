#!/bin/bash

# Function to check if a Python package is installed
function check_python_package {
    python3 -c "import $1" &> /dev/null
}

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "pip is not installed. Installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py --user
fi

# Check if venv module is available
if ! python3 -c "import venv" &> /dev/null; then
    echo "venv module not found. Installing python3-venv..."
    sudo apt-get update
    sudo apt-get install python3-venv
fi

# Create and activate a virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment (venv)..."
    python3 -m venv venv
fi

echo "Activating virtual environment (venv)..."
source venv/bin/activate

# Ensure pip is up-to-date inside the virtual environment
pip install --upgrade pip

# Check if Pandas is already installed
if ! check_python_package pandas; then
    echo "Installing Pandas..."
    pip install pandas
fi

# Now run your portaone_task.py script
echo "Running portaone_task.py..."
python3 portaone_task.py

# Deactivate the virtual environment
deactivate
