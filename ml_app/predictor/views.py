from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import HousePredictionForm
from .ml_model import HousePricePredictor
import pandas as pd

def predict_house_price(request):
    prediction = None
    form = HousePredictionForm()
    
    if request.method == 'POST':
        form = HousePredictionForm(request.POST)
        if form.is_valid():
            # Prepare input for prediction
            input_data = pd.DataFrame({
                'size': [form.cleaned_data['size']],
                'bedrooms': [form.cleaned_data['bedrooms']],
                'location_score': [form.cleaned_data['location_score']]
            })
            
            # Make prediction
            predictor = HousePricePredictor()
            try:
                prediction = predictor.predict(input_data)
            except Exception as e:
                prediction = f"Error: {str(e)}"
    
    return render(request, 'predictor/predict.html', {
        'form': form, 
        'prediction': prediction
    })