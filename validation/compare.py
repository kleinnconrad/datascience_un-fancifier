import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

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
    Note: The variables below are now Z-scores, not raw numbers.
    """
    pclass_std = row['Pclass']
    sex_female_std = row['Sex_Female']
    age_std = row['Age']
    fare_std = row['Fare']
    
    # --- REPLACE THESE CONDITIONS WITH YOUR NEW CLI OUTPUT ---
    if (pclass_std < -0.4653) or \
       (sex_female_std > 0.3760) or \
       (age_std < -0.9038) or \
       (fare_std > 4.7000):
        return 1  # Predict Survived
    else:
        return 0  # Predict Did Not Survive

def main():
    print("--- Loading and Standardizing Data ---")
    df = load_and_prep_titanic()
    
    X_raw = df[['Pclass', 'Sex_Female', 'Age', 'Fare']]
    y = df['Survived']
    
    # Scale the data so mean = 0 and std = 1
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X_raw), columns=X_raw.columns)
    
    print("--- Training Standardized Logistic Regression ---")
    # Initialize model with the specific standardized coefficients
    lr = LogisticRegression()
    lr.fit(X_scaled, y) 
    lr.intercept_ = np.array([-0.47])
    lr.coef_ = np.array([[-1.01, 1.25, -0.52, 0.10]])
    
    # Get original predictions from the scaled model
    lr_predictions = lr.predict(X_scaled)
    
    print("--- Applying Heuristic Rules ---")
    # Apply your custom rule to every scaled row
    rule_predictions = X_scaled.apply(predict_with_rules, axis=1)
    
    print("\n======================================================")
    print("                 PERFORMANCE COMPARISON")
    print("======================================================")
    
    # Evaluate Original Model
    cm_lr = confusion_matrix(y, lr_predictions)
    total_lr = np.sum(cm_lr)
    
    print("1. Standardized Logistic Regression:")
    print(f"   Accuracy:  {accuracy_score(y, lr_predictions) * 100:.2f}%")
    print(f"   Precision: {precision_score(y, lr_predictions) * 100:.2f}%")
    print(f"   Recall:    {recall_score(y, lr_predictions) * 100:.2f}%")
    print("   Confusion Matrix (Absolute & Relative):")
    print(f"      [TN: {cm_lr[0][0]:4d} ({cm_lr[0][0]/total_lr*100:4.1f}%) | FP: {cm_lr[0][1]:4d} ({cm_lr[0][1]/total_lr*100:4.1f}%)]")
    print(f"      [FN: {cm_lr[1][0]:4d} ({cm_lr[1][0]/total_lr*100:4.1f}%) | TP: {cm_lr[1][1]:4d} ({cm_lr[1][1]/total_lr*100:4.1f}%)]\n")
    
    # Evaluate Extracted Rules
    cm_rules = confusion_matrix(y, rule_predictions)
    total_rules = np.sum(cm_rules)
    
    print("2. Generated 'OR' Rules (from Standardized Data):")
    print(f"   Accuracy:  {accuracy_score(y, rule_predictions) * 100:.2f}%")
    print(f"   Precision: {precision_score(y, rule_predictions) * 100:.2f}%")
    print(f"   Recall:    {recall_score(y, rule_predictions) * 100:.2f}%")
    print("   Confusion Matrix (Absolute & Relative):")
    print(f"      [TN: {cm_rules[0][0]:4d} ({cm_rules[0][0]/total_rules*100:4.1f}%) | FP: {cm_rules[0][1]:4d} ({cm_rules[0][1]/total_rules*100:4.1f}%)]")
    print(f"      [FN: {cm_rules[1][0]:4d} ({cm_rules[1][0]/total_rules*100:4.1f}%) | TP: {cm_rules[1][1]:4d} ({cm_rules[1][1]/total_rules*100:4.1f}%)]")
    print("======================================================")

if __name__ == "__main__":
    main()
