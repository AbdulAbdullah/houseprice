from django import forms

class HousePredictionForm(forms.Form):
    size = forms.FloatField(
        label='House Size (sq ft)', 
        min_value=0, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    bedrooms = forms.IntegerField(
        label='Number of Bedrooms', 
        min_value=1, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    location_score = forms.FloatField(
        label='Location Score (1-10)', 
        min_value=1, 
        max_value=10, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )