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
