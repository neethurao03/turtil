# Nutrisoul
# Soil Health Analysis and Recommendation System

import pandas as pd
import numpy as np

def get_soil_data():
    return pd.DataFrame({
        'pH': [5.5, 6.0, 6.5, 7.0, 7.5, 8.0], 
        'Nitrogen': [30, 40, 50, 45, 35, 25],                             
        'Phosphorus': [20, 25, 30, 28, 22, 18],      
        'Potassium': [15, 18, 22, 20, 17, 12] 
    })

def get_crop_recommendations():
    return {
        (5.0, 6.0): 'Rice, Maize', 
        (6.0, 7.0): 'Wheat, Barley',
        (7.0, 8.0): 'Cotton, Sunflower'
    }

def recommend_fertilizers(nitrogen, phosphorus, potassium): 
    fertilizers = [] 
    if nitrogen < 40:
        fertilizers.append('Nitrogen Fertilizer (Urea)')
    if phosphorus < 25:       
        fertilizers.append('Phosphorus Fertilizer (DAP)') 
    if potassium < 20: 
        fertilizers.append('Potassium Fertilizer (MOP)')
   
    return fertilizers if fertilizers else ['No additional fertilizers needed']

def analyze_soil(pH_value): 
    soil_data = get_soil_data()  
    crop_recommendations = get_crop_recommendations()

    closest_match = soil_data.iloc[(soil_data['pH'] - pH_value).abs().argsort()[:1]]
    nitrogen = closest_match['Nitrogen'].values[0]
    phosphorus = closest_match['Phosphorus'].values[0]
    potassium = closest_match['Potassium'].values[0]

    recommended_crop = 'Not Available'
    for (low, high), crop in crop_recommendations.items():
        if low <= pH_value <= high:
            recommended_crop = crop
            break

    fertilizer_suggestion = recommend_fertilizers(nitrogen, phosphorus, potassium)

    return {
        'pH': pH_value,
        'Recommended Crop': recommended_crop,
        'Fertilizer Suggestion': fertilizer_suggestion,
        'Nutrient Levels': {
            'Nitrogen': nitrogen,
            'Phosphorus': phosphorus,
            'Potassium': potassium
        }
    }

def main():
    try: 
        pH_input = float(input('Enter soil pH value (5.0 to 8.0): ')) 
        if 5.0 <= pH_input <= 8.0: 
            result = analyze_soil(pH_input)    
            print('Analysis Result:', result)
        else: 
            print('Please enter a pH value within the range of 5.0 to 8.0.') 
    except ValueError: 
        print('Invalid input. Please enter a numeric value.')

if __name__ == "__main__":
    main()