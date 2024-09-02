# jobRad-coding-challenge-DevEx

## Overview
This project contains a Python script for merging intervals.
It allows users to input intervals in three different ways: 
- using a predefined set of intervals
- by entering them manually via the command line
- or by reading them from a file

## Setup Instructions

### Using Makefile (Recommended for Linux/MacOS users)
To set up the project and run tasks:
```bash
make install    # Install dependencies
make run        # Run the script with interactive input options
make test       # Execute tests
make clean      # Clean temporary files
```

### Using PowerShell (Recommended for Windows users)
To set up the project and run tasks using PowerShell:
```Powershell
.\build.ps1 -action install  # Install dependencies
.\build.ps1 -action run      # Run the script with interactive input options
.\build.ps1 -action test     # Execute tests
.\build.ps1 -action clean    # Clean temporary files
```

## Input Options
When running the script, you will be prompted to choose an input method:
1. Default Input: Use a predefined set of intervals.
2. Direct Input: Manually enter intervals via the command line.
3. File Input: Load intervals from a specified file (you can use the example_intervals.txt)

Follow the on-screen instructions after starting the script to provide the necessary input.

## Project Structure
- `src/merge_intervals.py`: Main script to merge intervals.
- `tests/test_merge_intervals.py`: Contains unit tests for the script.
- `Makefile`: Commands for Unix-based systems.
- `build.ps1`: PowerShell script for Windows.
- `requirements.txt`: Required Python packages.
- `.venv/`: Virtual environment directory (not included in version control).
