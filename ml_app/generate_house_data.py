import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Function to generate realistic house data
def generate_house_data(num_samples=10000):
    # Generate synthetic data
    data = {
        'size': np.random.normal(2000, 500, num_samples),  # Mean 2000 sq ft, std dev 500
        'bedrooms': np.random.randint(1, 6, num_samples),  # 1-5 bedrooms
        'bathrooms': np.random.randint(1, 4, num_samples),  # 1-3 bathrooms
        'location_score': np.random.uniform(1, 10, num_samples),  # Location desirability 1-10
        'year_built': np.random.randint(1950, 2023, num_samples),  # Year built
        'lot_size': np.random.normal(5000, 2000, num_samples),  # Mean 5000 sq ft lot, std dev 2000
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Generate price with some realistic correlations
    def calculate_price(row):
        base_price = 100000  # Base house price
        
        # Price factors
        size_factor = row['size'] * 150  # $150 per sq ft
        bedroom_factor = row['bedrooms'] * 25000  # Each bedroom adds value
        location_factor = row['location_score'] * 10000  # Location importance
        age_factor = max(0, (2023 - row['year_built']) * 1000)  # Older homes might depreciate
        lot_factor = row['lot_size'] * 10  # Additional lot size value
        
        # Add some randomness
        noise = np.random.normal(0, 50000)
        
        return base_price + size_factor + bedroom_factor + location_factor - age_factor + lot_factor + noise
    
    # Calculate prices
    df['price'] = df.apply(calculate_price, axis=1)
    
    # Ensure no negative prices
    df['price'] = df['price'].clip(lower=50000)
    
    return df

# Generate and save the dataset
house_data = generate_house_data(num_samples=50000)

# Save to CSV
house_data.to_csv('house_prices.csv', index=False)

# Print some basic statistics
print(house_data.describe())

# Verify the file was created
print("\nDataset saved to house_prices.csv")
print(f"Total number of records: {len(house_data)}")