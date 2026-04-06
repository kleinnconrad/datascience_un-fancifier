import math
import sys

def main():
    print("======================================================")
    print("  Logistic Regression to 'OR' Rule Converter CLI")
    print("======================================================")
    
    # 1. Get the number of coefficients
    while True:
        try:
            num_coeffs_str = input("\nEnter the total number of coefficients (including the constant/intercept): ")
            num_coeffs = int(num_coeffs_str)
            if num_coeffs >= 2:
                break
            print("Error: Please enter a number of 2 or greater (1 constant + at least 1 feature).")
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")

    # 2. Get the coefficients
    print("\n--- Enter Coefficients ---")
    while True:
        try:
            constant = float(input("Enter the constant (intercept): "))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            
    feature_coeffs = []
    for i in range(1, num_coeffs):
        while True:
            try:
                coef = float(input(f"Enter the coefficient for Feature {i}: "))
                feature_coeffs.append((f"Feature_{i}", coef))
                break
            except ValueError:
                print("Error: Invalid input. Please enter a number.")

    # 3. Get the cut-off point
    print("\n--- Enter Cut-off ---")
    while True:
        try:
            cutoff = float(input("Enter the probability cut-off point (e.g., 0.5): "))
            if 0 < cutoff < 1:
                break
            print("Error: Cut-off must be strictly greater than 0 and less than 1.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

    # 4. Math Translation: Convert probability to log-odds (z-score)
    z_cut = math.log(cutoff / (1.0 - cutoff))
    
    print("\n======================================================")
    print("                 GENERATED RULES")
    print("======================================================")
    print(f"Target Log-Odds (z) for a {cutoff} probability: {z_cut:.4f}\n")

    # 5. Extract rules
    rule_conditions = []
    
    for name, coef in feature_coeffs:
        if coef == 0:
            continue # Skip features with a weight of zero
            
        # Algebraically solve for the isolated threshold
        # z_cut = constant + (coef * feature_threshold)
        threshold = (z_cut - constant) / coef
        
        # Determine logical direction based on weight sign
        if coef > 0:
            rule_conditions.append(f"{name} > {threshold:.4f}")
        else:
            rule_conditions.append(f"{name} < {threshold:.4f}")
            
    # 6. Display the final statement
    if not rule_conditions:
        print("Result: No valid features to create rules from (all weights were 0).")
        sys.exit(0)
        
    complex_rule = " OR \n    ".join(rule_conditions)
    
    print("IF")
    print(f"    {complex_rule}")
    print("THEN")
    print("    Predict = True")
    print("======================================================")

if __name__ == "__main__":
    # Handle KeyboardInterrupt gracefully for CLI exits (Ctrl+C)
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting tool.")
        sys.exit(0)
