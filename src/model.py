import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv('../data/dataset.csv')

# Features & labels
X = data[['screen_time', 'social_media_hours', 'sleep_hours', 'study_hours']]
y = data['addiction_level']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Prediction function
def predict_addiction(input_data):
    return model.predict([input_data])[0]