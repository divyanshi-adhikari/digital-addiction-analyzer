# ScreenSense-AI

An AI-powered digital wellness assistant that analyzes screen usage patterns, predicts addiction risk levels, and provides personalized insights and practical suggestions to help users reduce excessive screen time and build healthier, more balanced digital habits in daily life.

##  The Problem

Today, the average person spends **6+ hours daily** on screens, often without realizing it. Excessive screen time can lead to:

- Poor sleep quality  
- Reduced productivity  
- Increased stress and anxiety  
- Weakening of real-life connections  

**ScreenSense AI** is designed to help users become more aware of their digital habits and take control of their screen time in a smarter and healthier way.

##  What It Does

| Feature | Description |
|---------|-------------|
|  **AI Prediction** | Uses a machine learning model to analyze your data and predict addiction risk levels (Low/Medium/High) |
|  **Smart Scoring** | Calculates a comprehensive 0–100 addiction score based on 7 key usage metrics |
|  **Personalized Insights** | Highlights critical issues, warning signs, and positive habits to give a clear understanding of your behavior |
|  **Actionable Suggestions** | Provides customized recommendations along with a practical 7-day improvement challenge |
|  **Progress Tracking** | Allows users to save results and track improvements in their screen habits over time |
|  **Visual Analytics** | Displays interactive charts to compare your usage patterns with healthy benchmarks |

##  How It Works

### 1. Enter Your Daily Habits
| Metric | Description |
|--------|-------------|
| Screen Time | Total device usage time |
| Social Media | Time on social apps |
| Gaming | Time spent gaming |
| Sleep | Hours slept per night |
| Study/Work | Productive time |
| Exercise | Physical activity time |
| Family Time | In-person interaction time |

### 2. AI Analyzes Your Data

### Scoring Formula

Addiction Score = (Screen × 8 + Social × 12 + Gaming × 7) - (Sleep × 6 + Study × 9 + Exercise × 5 + Family × 4) + 50

*Score is clamped between 0 and 100. Higher score = higher addiction risk.*

### 3. Get Instant Results

| Score | Risk Level | Action |
|-------|------------|--------|
| 65-100 | **HIGH** | Immediate intervention needed |
| 35-64 | **MEDIUM** | Changes recommended |
| 0-34 | **LOW** | Maintain healthy habits |

**Your Results Include:**
-  Addiction Score (0-100)
-  Risk Level with color coding
-  Personalized Insights (critical issues, warnings, positives)
-  Actionable Suggestions with 7-day challenge
-  Progress History to track improvement
-  Visual Analytics comparing your habits
-  AI Model Prediction from trained Decision Tree

---

### 4. Track Your Progress

Every analysis is saved locally. View your last 10 analyses and see trends:
-  Score improvement over time
-  Risk level changes
-  Habit pattern recognition

*Your data stays private on your device.*



##  Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit |
| **ML Model** | scikit-learn (Decision Tree Classifier) |
| **Data Processing** | Pandas |
| **Visualization** | Matplotlib |
| **Language** | Python 3.8+ |

##  Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/divyanshi-adhikari/screen-sense-ai.git
cd screen-sense-ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run src/main.py
```

### 4. Open Your Browser
Navigate to http://localhost:8501

##  Project Structure

```
screen-sense-ai/
│
├── src/
│   ├── main.py              # Streamlit application (UI + scoring + insights)
│   └── model.py             # ML model training & prediction
│
├── data/
│   └── dataset.csv          # Training data (Low/Medium/High)
│
├── images/                  # Screenshots for documentation
│   ├── main-interface.jpeg
│   ├── analysis-results-1.jpeg
│   ├── analysis-results-2.jpeg
│   ├── analysis-results-3.jpeg
│   ├── analysis-results-4.jpeg
│   ├── visualization.jpeg
│   └── history-tracking.jpeg
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── SCREENSHOTS.md          # Complete screenshots gallery
└── user_history.json       # Auto-generated (local history tracking)
```

##  Author

-Divyanshi Adhikari  
-1st year Btech CSE Student
