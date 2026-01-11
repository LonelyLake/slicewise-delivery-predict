set shell := ["powershell", "-Command"]

# Generate data for analysis
gen:
    uv run python src/generate_data.py

# Run Jupyter Lab for analysis
notebook:
    uv run jupyter lab