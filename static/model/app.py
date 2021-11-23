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

col='Mean_Salary', 'Python', 'R', 'SQL', 'AWS', 'Excel', 'GCP', 'Azure', 'Spark', 'Tableau', 'Keras', 'NoSQL', 'Machine_Learning', 'Hadoop', 'AI', 'Power_BI', 'Job Title_data analyst', 'Job Title_data engineer', 'Job Title_data science related jobs', 'Job Title_data scientist', 'Job Title_director', 'Job Title_machine learning engineer', 'Job Title_manager', 'Category_Big Data Software Engineer', 'Category_Business Intelligence Analyst', 'Category_Business Intelligence Developer', 'Category_Business Systems Analyst', 'Category_Data Analyst', 'Category_Data Architect', 'Category_Data Engineer', 'Category_Data Modeler', 'Category_Data Scientist', 'Category_Data Storyteller', 'Category_Data Warehouse Manager', 'Category_Database Administrator', 'Category_Database Manager', 'Category_IT Systems Analyst', 'Category_Logistics Analyst', 'Category_Machine Learning Engineer', 'Category_Machine Learning Scientist', 'Category_Marketing Analyst', 'Category_Quantitative Analyst', 'Category_Statistician', 'state_ AK', 'state_ AL', 'state_ AR', 'state_ AZ', 'state_ CA', 'state_ CO', 'state_ CT', 'state_ DC', 'state_ DE', 'state_ FL', 'state_ GA', 'state_ HI', 'state_ IA', 'state_ ID', 'state_ IL', 'state_ IN', 'state_ KS', 'state_ KY', 'state_ LA', 'state_ MA', 'state_ MD', 'state_ ME', 'state_ MI', 'state_ MN', 'state_ MO', 'state_ MS', 'state_ MT', 'state_ NC', 'state_ NE', 'state_ NH', 'state_ NJ', 'state_ NM', 'state_ NV', 'state_ NY', 'state_ OH', 'state_ OK', 'state_ OR', 'state_ PA', 'state_ RI', 'state_ SC', 'state_ TN', 'state_ TX', 'state_ UT', 'state_ VA', 'state_ VI', 'state_ VT', 'state_ WA', 'state_ WI', 'state_ WV', 'state_ WY', 'Seniority_Not Specified', 'Seniority_Senior'

def salary_category(bin):

    if bin==1:
        return "Job salary is estimated be between $50000 and $75000"
    if bin==2:
        return "Job salary is estimated be between $75000 and $100000"
    if bin==3:
        return "Job salary is estimated be between $100000 and $125000"
    if bin==4:
        return "Job salary is estimated be between $125000 and $150000"
    if bin==5:
        return "Job salary is estimated be between $150000 and $175000"
    if bin==6:
        return "Job salary is estimated be between $175000 and $200000"
    if bin==7:
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
