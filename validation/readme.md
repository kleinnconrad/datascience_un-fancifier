#The generated if-then-else ruleset derived from a standardized logistic regression function based on the titanic dataset:

```
======================================================
  Logistic Regression to 'OR' Rule Converter CLI
======================================================

Enter the total number of coefficients (including the constant/intercept): 5

--- Enter Coefficients ---
Enter the constant (intercept): -0.47
Enter the coefficient for Feature 1: -1.01
Enter the coefficient for Feature 2: 1.25
Enter the coefficient for Feature 3: -0.52
Enter the coefficient for Feature 4: 0.10

--- Enter Cut-off ---
Enter the probability cut-off point (e.g., 0.5): 0.7

======================================================
                 GENERATED RULES
======================================================
Target Log-Odds (z) for a 0.7 probability: 0.8473

IF
    Feature_1 < -1.3043 OR
    Feature_2 > 1.0538 OR
    Feature_3 < -2.5333 OR
    Feature_4 > 13.1730
THEN
    Predict = True
======================================================
```
# The result is quite okay-ish
If you are not satisfied with the performance just play a bit around with the cut-off point. Also remember to feed the tool with standardized logistic regression functions!

```
--- Loading and Standardizing Data ---
--- Training Standardized Logistic Regression ---
--- Applying Heuristic Rules ---

======================================================
                 PERFORMANCE COMPARISON
======================================================
1. Standardized Logistic Regression:
   Accuracy:  79.46%
   Precision: 71.66%
   Recall:    76.90%
   Confusion Matrix (Absolute & % of Actual Class):
      [TN:  445 (81.1%) | FP:  104 (18.9%)]
      [FN:   79 (23.1%) | TP:  263 (76.9%)]

2. Generated 'OR' Rules (from Standardized Data):
   Accuracy:  75.08%
   Precision: 63.76%
   Recall:    81.29%
   Confusion Matrix (Absolute & % of Actual Class):
      [TN:  391 (71.2%) | FP:  158 (28.8%)]
      [FN:   64 (18.7%) | TP:  278 (81.3%)]
======================================================
```
