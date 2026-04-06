# Unfancify LR: Logistic Regression to Legacy Ruleset Converter

A CLI tool that reverse-engineers a trained logistic regression model into readable `IF A OR B OR C THEN True` statements. It is designed to bridge the gap between modern data science and legacy software, translating a linear model's weights into independent logical thresholds for systems that cannot process linear algebra.

## Table of Contents
- [Critical Requirement: Standardized Data](#critical-requirement-standardized-data)
- [How to Use It](#how-to-use-it)
- [Tuning Performance: The Cut-Off Point](#tuning-performance-the-cut-off-point)
- [Validation: The Titanic Dataset](#validation-the-titanic-dataset)
- [Contribute to Unfancifying Data Science](#contribute-to-unfancifying-data-science)

## Critical Requirement: Standardized Data

Your logistic regression model must be trained on standardized data (scaled using a `StandardScaler` to a mean of `0` and a standard deviation of `1`). 

To extract an independent rule for a single feature, the tool assumes all other features are at their baseline. With standardized data, an input of `0` represents the actual mathematical average, ensuring accurate and realistic thresholds.

## How to Use It

1. Run the script: `python unfancifier.py`
2. Enter the total number of coefficients in your model (including the intercept).
3. Enter the constant (intercept) and the weights for each feature.
4. Enter your desired probability cut-off (e.g., `0.7`).

The tool will output a clean set of `IF... OR...` rules using the calculated Z-score thresholds.

## Tuning Performance: The Cut-Off Point

Forcing an additive mathematical model into a flat boolean `OR` structure inherently changes its behavior. `OR` logic is highly permissive, destroying a linear model's ability to compensate negatively. A standard `0.5` cut-off often yields fantastic Recall but low Specificity (too many False Positives).

**The Fix:** Increase the probability cut-off point (e.g., to `0.70`). Raising the target cut-off artificially tightens the threshold required for any single feature to trigger a `True` prediction, restoring the balance between Precision and Recall.

## Validation: The Titanic Dataset

We validated this heuristic methodology against a standardized logistic regression model trained to predict passenger survival on the Titanic dataset. By tuning the CLI tool to a `0.7` cut-off, we generated an `OR` ruleset and compared its predictive power against the original model:

* **Original Logistic Regression:** 79.46% Accuracy | 81.1% True Negatives | 76.90% True Positives (Recall)
* **Generated 'OR' Rules (0.7 Cut-off):** 75.08% Accuracy | 71.2% True Negatives | 81.29% True Positives (Recall)

The tuned ruleset successfully mirrors the original model's performance footprint while remaining entirely in flat boolean logic. For evaluation scripts and detailed confusion matrices, see the `validation/` folder.

## Contribute to Unfancifying Data Science

Sometimes the best solution is a mathematically sound heuristic that can run safely inside a legacy system. Fork this repository and help us build out new features.
