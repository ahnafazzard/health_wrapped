#!/bin/bash

# Create the conda environment
echo "Creating conda environment..."
conda env create -f environment.yml

echo "Setup complete! To activate this environment, run: conda activate health-app"