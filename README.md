Title:MLA In UAVs
docs/= We will use this folder to store the important documents related to our research 
src/= For storing models and modules
data/= For storing the data collected for experiments
results/= For storing the results of experiments
refernces/= For storing the citated paper
# PhD Research Workflow Project

## Project Structure
- data/ → raw and cleaned datasets
- src/ → scripts (cleaning & visualization)
- results/ → generated plots
- docs/ → documentation files

## Files and Folders
- sample_data.csv → raw dataset
- cleaned_data.csv → processed dataset
- clean_data.py → data cleaning script
- visualize_data.py → visualization script

## How to Run
1. Run cleaning:
   python src/clean_data.py
2. Run visualization:
   python src/visualize_data.py

## Expected Outputs
- cleaned dataset
- score_plot.png
- temp_humidity_plot.png

## Assumptions
- Missing values handled using mean imputation
- Dataset is numeric

## Future Scope
- Try median imputation
- Add ML models
- Improve visualization
