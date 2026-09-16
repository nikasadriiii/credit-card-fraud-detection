# Credit Card Fraud Detection

## Overview

A machine learning project for detecting fraudulent credit card
transactions using an imbalanced transaction dataset.

## Dataset

The dataset contains credit card transactions with anonymized
features and a binary fraud target.

- 0 = Normal transaction
- 1 = Fraudulent transaction

## Project Workflow

1. Data loading
2. Exploratory data analysis
3. Class imbalance analysis
4. Train/test split
5. Data preprocessing
6. Baseline Logistic Regression
7. Baseline Random Forest
8. SMOTE oversampling
9. Logistic Regression + SMOTE
10. Random Forest + SMOTE
11. Model evaluation
12. Feature importance analysis
13. Model persistence
14. SQL analysis

## Models

### Logistic Regression

Used as a baseline classification model.

### Random Forest

Used as the primary nonlinear classification model.

### SMOTE

SMOTE was applied only to the training data to address severe
class imbalance while keeping the test set representative of
real-world data.

## Evaluation Metrics

Because fraud detection is highly imbalanced, the project focuses
on:

- Precision
- Recall
- F1-Score
- PR-AUC

Accuracy is reported but is not treated as the primary metric.

## Results

Final Random Forest + SMOTE results:

- Accuracy: ADD YOUR RESULT
- Precision: ADD YOUR RESULT
- Recall: ADD YOUR RESULT
- F1-Score: ADD YOUR RESULT
- PR-AUC: ADD YOUR RESULT

## Project Structure

```text
credit-card-fraud-detection/
│
├── data/
│   └── creditcard.csv
│
├── models/
│   ├── random_forest_smote.pkl
│   └── feature_names.pkl
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── sql/
│   └── fraud_analysis.sql
│
├── src/
│   ├── load_data.py
│   └── predict.py
│
└── README.md