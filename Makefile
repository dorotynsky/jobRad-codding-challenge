# Install dependencies
install:
	.venv\Scripts\pip install -r requirements.txt

# Run the main script
run:
	.venv\Scripts\python src/merge_intervals.py

# Run the tests
test:
	.venv\Scripts\python -m unittest discover -s tests

# Clean up temporary files and caches
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
