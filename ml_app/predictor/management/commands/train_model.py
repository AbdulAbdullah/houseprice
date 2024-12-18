from django.core.management.base import BaseCommand
from predictor.ml_model import HousePricePredictor

class Command(BaseCommand):
    help = 'Train the house price prediction machine learning model'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting model training...')
        
        try:
            predictor = HousePricePredictor()
            mse = predictor.train_model()
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Model trained successfully. Mean Squared Error: {mse}'
                )
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(
                    f'Model training failed: {str(e)}'
                )
            )