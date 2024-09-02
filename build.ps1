param (
    [string]$action
)

switch ($action) {
    "install" {
        .venv\Scripts\pip install -r requirements.txt
    }
    "run" {
        .venv\Scripts\python src/merge_intervals.py
    }
    "test" {
        .venv\Scripts\python -m unittest discover -s tests
    }
    "clean" {
        Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force
    }
    default {
        Write-Host "Usage: .\build.ps1 -action [install|run|test|clean]"
    }
}
