# jobRad-coding-challenge-DevEx

## Overview
This project contains a Python script for merging intervals.

## Setup Instructions

### Using Makefile (Recommended for Linux/MacOS users)
To set up the project and run tasks:
```bash
make install    # Install dependencies
make run        # Run the script
make test       # Execute tests
make clean      # Clean temporary files
```

### Using PowerShell (Recommended for Windows users)
To set up the project and run tasks using PowerShell:
```Powershell
.\build.ps1 -action install  # Install dependencies
.\build.ps1 -action run      # Run the script
.\build.ps1 -action test     # Execute tests
.\build.ps1 -action clean    # Clean temporary files
```

## Project Structure

- `src/merge_intervals.py`: Main script to merge intervals.
- `tests/test_merge_intervals.py`: Contains unit tests for the script.
- `Makefile`: Commands for Unix-based systems.
- `build.ps1`: PowerShell script for Windows.
- `requirements.txt`: Required Python packages.
- `.venv/`: Virtual environment directory (not included in version control).
