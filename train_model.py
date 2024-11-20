import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

# Create a simple dummy model
def create_simple_model():
    # Create a basic model with minimal training
    model = RandomForestRegressor(n_estimators=10, random_state=42)
    
    # Generate tiny dummy dataset
    X = np.random.rand(10, 4)  # 10 samples, 4 features
    y = np.random.rand(10)     # 10 target values
    
    # Quick fit
    model.fit(X, y)
    
    # Create model directory if it doesn't exist
    os.makedirs('model', exist_ok=True)
    
    # Save the model
    with open('model/aqi_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("Simple model created and saved!")

if __name__ == "__main__":
    create_simple_model()
