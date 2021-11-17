from flask import Flask, render_template, redirect
from flask import request
import pandas as pd
import pickle


# Use pickle to load in the pre-trained model.
with open(f'static/model/salary_predict_model.pkl', 'rb') as f:

    model = pickle.load(f)


app = Flask(__name__)

@app.route("/")
def index():
    listings = {'_id':'615f3911a6d569a7cd86c945',
 'url': 'https://www.cnbc.com/2021/10/04/here-are-the-five-most-valuable-college-majors-.html',
 'img': 'https://image.cnbcfm.com/api/v1/image/106885838-1621509859148-gettyimages-1318999756-vcg111330726320.jpeg?v=1633354738&w=929&h=523',
 'title': 'Here are the 5 most valuable — and 5 least valuable — college majors'}
    return render_template("index.html",listings=listings)

@app.route("/slides")
def slides():
    return render_template("slides.html")

@app.route("/job_cat")
def jm():
    return render_template("jobs_by_category_mw.html")
    

@app.route("/job_market")
def jc():
    return render_template("job_market_map_visual_mw.html")
    

@app.route("/salary")
def sa():
    return render_template("as_charts.html")

@app.route("/employment_info")
def ei():
    return render_template("as_map.html")

@app.route('/salary_prediction',methods=['GET', 'POST'])
def sp():
    if request.method == 'GET':
        return render_template('salary_prediction_sj.html')
    if request.method == 'POST':
        temperature = request.form['temperature']
        humidity = request.form['humidity']
        windspeed = request.form['windspeed']
        input_variables = pd.DataFrame([[temperature, humidity, windspeed]],
                                       columns=['temperature', 'humidity', 'windspeed'],
                                       dtype=float)
        prediction = model.predict(input_variables)[0]
        return render_template('salary_prediction_sj.html',
                                     original_input={'Temperature':temperature,
                                                     'Humidity':humidity,
                                                     'Windspeed':windspeed},
                                     result=prediction,
                                     )
    

# @app.route("/scrape")
# def scraper():
#     mongo.db.listings.drop()
#     listings = mongo.db.listings
#     listings_data = scrape.scrape()
#     listings.update({}, listings_data, upsert=True)
#     return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
