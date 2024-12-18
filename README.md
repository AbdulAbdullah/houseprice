# House Price Prediction Django App

## Overview
This Django application provides a machine learning-powered web interface for predicting house prices based on key features such as size, number of bedrooms, and location score.

## Features
- Machine learning model for house price prediction
- Django web interface for easy interaction
- Synthetic dataset generation
- Model training and retraining capabilities

## Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/AbdulAbdullah/houseprice.git
cd house-price-predictor
```

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Generate Dataset For Test
```bash
python generate_house_data.py
```

### 5. Train Initial Machine Learning Model
```bash
python manage.py train_model
```

### 6. Run Migrations
```bash
python manage.py migrate
```

### 7. Start the Development Server
```bash
python manage.py runserver
```

## Usage
1. Navigate to `http://127.0.0.1:8000/` in your web browser
2. Enter house details:
   - House Size (sq ft)
   - Number of Bedrooms
   - Location Score (1-10)
3. Click "Predict Price" to get the estimated house price

## Retraining the Model
To retrain the model with new or updated data:
```bash
python manage.py train_model
```

## Model Details
- Algorithm: Random Forest Regressor
- Features: 
  - House Size
  - Number of Bedrooms
  - Location Score
- Evaluation Metric: Mean Squared Error

## Customization
- Modify `predictor/ml_model.py` to change machine learning approach
- Update `predictor/forms.py` to add or remove input fields
- Adjust price calculation in dataset generation script

## Troubleshooting
- Ensure all dependencies are installed
- Check that `house_prices.csv` is generated before training
- Verify Python and Django versions are compatible

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Your Name - abdulabdullah1000@gmail.com

Project Link: [https://github.com/AbdulAbdullah/houseprice.git](https://github.com/AbdulAbdullah/houseprice.git)