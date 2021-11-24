from flask import Flask, render_template, redirect
from flask import request
import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import FeatureUnion
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import joblib


class TextSelector(BaseEstimator, TransformerMixin):
    """
    Transformer to select a single column from the data frame to perform additional transformations on
    Use on text columns in the data
    """
    def __init__(self, key):
        self.key = key

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.key]
    
class NumberSelector(BaseEstimator, TransformerMixin):
    """
    Transformer to select a single column from the data frame to perform additional transformations on
    Use on numeric columns in the data
    """
    def __init__(self, key):
        self.key = key

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[[self.key]]

def salary_category(bin):

    if bin==1:
        return "Job salary is estimated be below $120000"
    if bin==2:
        return "Job salary is estimated be between $120000 and $160000"
    if bin==3:
        return "Job salary is estimated be between $160000 and $200000"
    if bin==4:
        return "Job salary is estimated be more than $200000"

def skill_check(dict):
    v=dict.values()
    skill_dict={
    'Python':0, 'R':0, 'SQL':0, 'AWS':0, 'Excel':0, 'GCP':0, 'Azure':0, 'Spark':0,
        'Tableau':0, 'Keras':0, 'NoSQL':0,
       'Machine_Learning':0, 'Hadoop':0
    }
    for i in v:
        if (i in skill_dict.keys()):
            skill_dict[i]=1
    return skill_dict

# Use pickle to load in the pre-trained model.
model=joblib.load( 'salary_predict_model.pkl')

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        names = request.form.to_dict()
        skill=skill_check(names)
        input=[names["titles"],names["size"],names["industry"],names["state"],names["age"]]
        input=input+list(skill.values())
        input=input+[names["titles"],names["seniority"]]
        df=pd.DataFrame([input],columns=['Job Title', 'Size',  'Industry',  'State','Age',
        'Python', 'R', 'SQL', 'AWS', 'Excel', 'GCP', 'Azure', 'Spark',
       'Tableau', 'Keras', 'NoSQL',
       'Machine_Learning', 'Hadoop', 'Job',
       'Seniority'])
        pred=salary_category( model.predict(df)[0])
        return render_template('index.html',pred=pred)
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
