import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

def load_and_prep_titanic():
    """Loads a public Titanic dataset and applies standard preprocessing."""
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    
    # Select our 4 features and the target
    df = df[['Survived', 'Pclass', 'Sex', 'Age', 'Fare']].copy()
    
    # Handle Missing Values (Fill Age with median)
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    
    # Convert Sex to binary (Female = 1, Male = 0)
    df['Sex_Female'] = (df['Sex'] == 'female').astype(int)
    df = df.drop('Sex', axis=1)
    
    return df

def predict_with_rules(row):
    """
    PASTE YOUR CLI TOOL LOGIC HERE.
    The rule below is just a placeholder structure.
    Replace the thresholds with what your CLI tool outputs.
    """
    # Example structure based on an OR rule:
    # IF Pclass < X OR Sex_Female > Y OR Age < Z OR Fare > W THEN True
    
    pclass = row['Pclass']
    sex_female = row['Sex_Female']
    age = row['Age']
    fare = row['Fare']
    
    # --- REPLACE THESE CONDITIONS WITH YOUR CLI OUTPUT ---
    if (pclass < 2.0833) or \
       (sex_female > -0.9615) or \
       (age < 62.5000) or \
       (fare > -1250.0000):
        return 1  # Predict Survived
    else:
        return 0  # Predict Did Not Survive

def main():
    print("--- Loading Data ---")
    df = load_and_prep_titanic()
    
    X = df[['Pclass', 'Sex_Female', 'Age', 'Fare']]
    y = df['Survived']
    
    print("--- Training Original Logistic Regression ---")
    # We force the coefficients to match the ones provided to you
    # so the comparison is mathematically exact.
    lr = LogisticRegression()
    lr.fit(X, y) # Fit just to initialize the classes
    lr.intercept_ = np.array([2.50])
    lr.coef_ = np.array([[-1.20, 2.60, -0.04, 0.002]])
    
    # Get original predictions
    lr_predictions = lr.predict(X)
    
    print("--- Applying Heuristic Rules ---")
    # Apply your custom rule to every row
    rule_predictions = df.apply(predict_with_rules, axis=1)
    
    print("\n======================================================")
    print("                 PERFORMANCE COMPARISON")
    print("======================================================")
    
    # Evaluate Original Model
    print("1. Original Logistic Regression:")
    print(f"   Accuracy:  {accuracy_score(y, lr_predictions) * 100:.2f}%")
    print(f"   Precision: {precision_score(y, lr_predictions) * 100:.2f}%")
    print(f"   Recall:    {recall_score(y, lr_predictions) * 100:.2f}%\n")
    
    # Evaluate Extracted Rules
    print("2. Generated 'OR' Rules:")
    print(f"   Accuracy:  {accuracy_score(y, rule_predictions) * 100:.2f}%")
    print(f"   Precision: {precision_score(y, rule_predictions) * 100:.2f}%")
    print(f"   Recall:    {recall_score(y, rule_predictions) * 100:.2f}%")
    print("======================================================")

if __name__ == "__main__":
    main()
