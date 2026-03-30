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