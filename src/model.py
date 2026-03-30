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

# Add score and risk
def calculate_score(screen_time, social_media, sleep, study):
    score = (screen_time*10 + social_media*10) - (sleep*5 + study*5)
    return max(0, min(100, score))

score = calculate_score(screen_time, social_media, sleep, study)

print(f"Addiction Score: {score}/100")

if score > 70:
    risk = "HIGH "
elif score > 40:
    risk = "MEDIUM"
else:
    risk = "LOW "

print("Risk Level:", risk)

    