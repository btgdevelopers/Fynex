import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from .DiseasePredictor import DiseasePredictor
from .ContentRecommenderNutrition import ContentRecommenderNutrition
from .ContentRecommenderExercise import ContentRecommenderExercise
import math

class HybridRecommender:

    def __init__(self):
        self.disease_predictor = DiseasePredictor()
        self.content_recommender_nutrition = ContentRecommenderNutrition()
        self.content_recommender_exercise = ContentRecommenderExercise()
    
    def predictDiseases(self,heartRate, glucose, height, weight, age):
        bmi = weight/math.pow(height,2)
        res_disease = self.disease_predictor.predictDisease(heartRate,glucose,bmi,age)
        res_disease = res_disease[res_disease['Proba']>0.5]
        diseases = res_disease['Disease'].values
        return diseases
    
    def predictNutrition(self,heartRate, glucose, height, weight, age):
        diseases = self.predictDiseases(heartRate, glucose, height, weight, age)
        degrees_freedom = 0.3 if len(diseases) == 0 else 0.1
        diseases = ['normal'] if len(diseases) == 0 else diseases
        res = self.content_recommender_nutrition.predict(diseases,degrees_freedom)
        return {'diseases':diseases,'recommendations':res[0],'diff':res[1]}
    
    def predictExercise(self,heartRate, glucose, height, weight, age):
        diseases = self.predictDiseases(heartRate, glucose, height, weight, age)
        diseases = ['normal'] if len(diseases) == 0 else diseases
        res = self.content_recommender_exercise.predict(diseases[0])
        return {'diseases':diseases,'recommendations':res}



