# Install project dependencies
install:
	venv/bin/pip install -r requirements.txt

# Run the main script
run:
	venv/bin/python src/merge_intervals.py

# Run unit tests
test:
	venv/bin/python -m unittest discover -s tests

# Clean up temporary files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
