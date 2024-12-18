import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import os

class HousePricePredictor:
    def __init__(self, model_path='house_price_model.joblib'):
        self.model_path = model_path
        self.model = None

    def train_model(self, data_path='house_prices.csv'):
        # Load data
        housing_data = pd.read_csv(data_path)
        
        # Prepare features and target
        X = housing_data[['size', 'bedrooms', 'location_score']]
        y = housing_data['price']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train model
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Mean Squared Error: {mse}")
        
        # Save model
        joblib.dump(self.model, self.model_path)
        return mse

    def predict(self, house_features):
        # Load model if not already loaded
        if self.model is None:
            if os.path.exists(self.model_path):
                self.model = joblib.load(self.model_path)
            else:
                raise ValueError("No trained model found. Please train the model first.")
        
        # Validate input
        required_features = ['size', 'bedrooms', 'location_score']
        if not all(feature in house_features.columns for feature in required_features):
            raise ValueError(f"Input must contain columns: {required_features}")
        
        return self.model.predict(house_features)[0]