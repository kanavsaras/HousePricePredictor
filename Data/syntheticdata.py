import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

def generate_house_data(num_samples):
    data = {
        'SquareFeet': np.random.randint(600, 4000, num_samples),
        'Bedrooms': np.random.randint(1, 6, num_samples),
        'Bathrooms': np.random.randint(1, 4, num_samples),
        'Age': np.random.randint(0, 50, num_samples),
        'LocationScore': np.random.randint(1, 11, num_samples) # Scale 1-10
    }
    
    df = pd.DataFrame(data)
    
    # The Exact Linear Formula
    df['Price'] = (
        (df['SquareFeet'] * 100) + 
        (df['Bedrooms'] * 20000) + 
        (df['Bathrooms'] * 15000) + 
        (df['LocationScore'] * 10000) - 
        (df['Age'] * 1000) + 
        50000 # Base Intercept
    )
    return df

# 1. Create 500 Training Examples
train_df = generate_house_data(500)
train_df.to_csv('housing_train_500.csv', index=False)
print(f"Successfully created 'housing_train_500.csv' with {len(train_df)} rows.")

# 2. Create specific Test Examples (for verification)
# We manually define these to ensure edge cases are covered
test_data = [
    # Small house, bad location, old
    [800, 1, 1, 30, 2], 
    # Average house, avg location
    [1500, 3, 2, 10, 5], 
    # Large house, prime location, new
    [3000, 5, 4, 0, 10], 
    # High age but great location
    [2000, 3, 2, 50, 9] 
]
columns = ['SquareFeet', 'Bedrooms', 'Bathrooms', 'Age', 'LocationScore']
test_df = pd.DataFrame(test_data, columns=columns)

# Apply same formula to get true price for checking
test_df['Price'] = (
    (test_df['SquareFeet'] * 100) + 
    (test_df['Bedrooms'] * 20000) + 
    (test_df['Bathrooms'] * 15000) + 
    (test_df['LocationScore'] * 10000) - 
    (test_df['Age'] * 1000) + 
    50000
)

test_df.to_csv('housing_test.csv', index=False)
print("Successfully created 'housing_test.csv' with manual verification cases.")