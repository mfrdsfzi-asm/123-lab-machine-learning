# 1_Regression_Model

This folder contains a comprehensive notebook and supporting files for building, analyzing, and evaluating regression models using Python and popular data science libraries.

## Contents
### 1. Regression Model Notebook
- `regression_model.ipynb`: Jupyter notebook covering the full workflow for regression analysis, including:
  - Data loading and inspection
  - Exploratory Data Analysis (EDA)
  - Data cleaning, imputation, and outlier handling
  - Feature engineering (normalization, encoding, binning)
  - Model evaluation (MSE, MAE)
  - Model training (Simple Linear Regression)
- Extras
  - Sample Polynomial Linear Regression Model
  - Model export and prediction
  - Quick prototyping with PyCaret


### 2. Sample API 
- `main.py`: Sample FastAPI boiler plate with Regression Model Deployment
#### How to Run the API

```bash
# Get into the directory
cd 1_Regression_Model

# Run the FastAPI
python main.py
```

This command will start the FastAPI server locally. By default, it will be available at [http://127.0.0.1:8003](http://127.0.0.1:8003).

![Testing the sampleAPI](/.devcontainer/postman_sample_api_lr_model.jpg)
