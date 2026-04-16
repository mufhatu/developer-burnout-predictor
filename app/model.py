import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

# directory where model.py lives → app/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# directory where model.py lives → app/
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    BASE_DIR, "..", "data", "developer_burnout_dataset_7000.csv"
)

MODEL_PATH = os.path.join(SCRIPT_DIR, "model.pkl")

  #labels for output 
Labels = {0: 'Low', 1: 'Medium', 2: 'High'}

def load_data():

    df = pd.read_csv(DATA_PATH)

    #drop missing target (NaN values)
    df = df.dropna(subset=['burnout_level'])
   
    #target vector
    y = df['burnout_level'].map({'Low':0, 'Medium':1,'High':2}).values
    
    #input matrix
    X = np.array([
        df['age'].values,
        df['experience_years'].values,
        df['daily_work_hours'].values,
        df['sleep_hours'].values,
        df['caffeine_intake'].values,
        df['bugs_per_day'].values,
        df['commits_per_day'].values,
        df['meetings_per_day'].values,
        df['screen_time'].values,
        df['exercise_hours'].values,
        df['stress_level'].values
    ]).T

    return X, y


#training function
def evaluate(model,X,y):
    cv= KFold(5, shuffle=True, random_state=42)

    scores = []
    for training, testing in cv.split(X):
        model.fit(X[training],y[training])
        yhat = model.predict(X[testing])
        acc_testing = accuracy_score(y[testing],yhat)
        scores.append(acc_testing)

    return np.mean(scores)

def train_save():
    X, y = load_data()
    model = RandomForestClassifier(max_depth=5,random_state=42)
    score = evaluate(model, X, y)
    print(f"Accuracy score: {score:.4f}")

    #retain the full data before saving
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    print("Model Saved")

def predict_burnout(metrics):

    #load trained model
    model = joblib.load(MODEL_PATH)

    #build matrix from API request
    X = np.array([[
        metrics.age,
        metrics.experience_years,
        metrics.daily_work_hours,
        metrics.sleep_hours,
        metrics.caffeine_intake,
        metrics.bugs_per_day,
        metrics.commits_per_day,
        metrics.meetings_per_day,
        metrics.screen_time,
        metrics.exercise_hours,
        metrics.stress_level
    ]])

    #pass matrix through the 100 decision trees
    predict = model.predict(X)[0]

    #get the probability for each class
    proba = model.predict_proba(X)[0][predict]

    return {
        "burnout_level": Labels[predict],"confidence":round(float(proba),3)
    }

if __name__ == "__main__":
    train_save()