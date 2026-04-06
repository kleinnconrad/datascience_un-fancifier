#The generated if-then-else ruleset derived from a logistic regression function based on the titanic dataset:

```
======================================================
  Logistic Regression to 'OR' Rule Converter CLI
======================================================

Enter the total number of coefficients (including the constant/intercept): 5

--- Enter Coefficients ---
Enter the constant (intercept): 2.5
Enter the coefficient for Feature 1: -1.2
Enter the coefficient for Feature 2: 2.6
Enter the coefficient for Feature 3: -0.04
Enter the coefficient for Feature 4: 0.002

--- Enter Cut-off ---
Enter the probability cut-off point (e.g., 0.5): 0.5

======================================================
                 GENERATED RULES
======================================================
Target Log-Odds (z) for a 0.5 probability: 0.0000

IF
    Feature_1 < 2.0833 OR
    Feature_2 > -0.9615 OR
    Feature_3 < 62.5000 OR
    Feature_4 > -1250.0000
THEN
    Predict = True
======================================================
```
