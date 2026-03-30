import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import os

# Load dataset using correct path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(BASE_DIR, 'data', 'dataset.csv')

data = pd.read_csv(data_path)

# Features & labels
X = data[['screen_time', 'social_media_hours', 'sleep_hours', 'study_hours']]
y = data['addiction_level']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Prediction function
def predict_addiction(input_data):
    import pandas as pd
    
    columns = ['screen_time', 'social_media_hours', 'sleep_hours', 'study_hours']
    input_df = pd.DataFrame([input_data], columns=columns)
    
    return model.predict(input_df)[0]

import streamlit as st

st.title("MindTrack AI - Digital Addiction Analyzer")

# INPUT
screen_time = st.slider("Screen Time", 0.0, 12.0, 5.0)
social_media = st.slider("Social Media Hours", 0.0, 8.0, 2.0)
sleep = st.slider("Sleep Hours", 0.0, 10.0, 7.0)
study = st.slider("Study Hours", 0.0, 10.0, 4.0)


# SCORE FUNCTION
def calculate_score(screen_time, social_media, sleep, study):
    score = (screen_time*10 + social_media*10) - (sleep*5 + study*5)
    return max(0, min(100, score))

score = calculate_score(screen_time, social_media, sleep, study)

print(f"Addiction Score: {score}/100")

# RISK LEVEL
if score > 70:
    risk = "HIGH "
elif score > 40:
    risk = "MEDIUM"
else:
    risk = "LOW "

print("Risk Level:", risk)

# INSIGHTS 
print("\nInsights:")

if screen_time > 6:
    print("- Excessive screen time detected")
if social_media > 3:
    print("- High social media usage")
if sleep < 6:
    print("- Poor sleep cycle affecting health")
if study < 3:
    print("- Low study time")

print(f"\nYour addiction score is {score}/100.")

# SUGGESTION
print("\nSuggestions:")

if score > 70:
    print("- Reduce screen time by 2-3 hours")
    print("- Avoid phone before sleep")
elif score > 40:
    print("- Balance study and phone usage")
else:
    print("- Maintain your healthy habits")

