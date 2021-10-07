from flask import Flask, render_template, redirect
# from flask_pymongo import PyMongo
# import scrape
from pymongo import MongoClient

app = Flask(__name__)
client=MongoClient("mongodb+srv://shan_jiang:jiangshan9678@cluster0.tutpa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.get_database("project3_DB")
list1=db.job_web

# # Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/job_news"
# mongo = PyMongo(app)
# mongo.db.listings.drop()

@app.route("/")
def index():
    listings = list1.find_one()
    return render_template("index.html",listings=listings)

@app.route("/slides")
def slides():
    return render_template("slides.html")

@app.route("/job_market")
def jm():
    return render_template("jobs_by_category_mw.html")
    

@app.route("/job_cat")
def jc():
    return render_template("job_market_map_mw.html")
    

@app.route("/salary")
def sa():
    return render_template("as_charts.html")

@app.route("/employment_info")
def ei():
    return render_template("as_map.html")


# @app.route("/scrape")
# def scraper():
#     mongo.db.listings.drop()
#     listings = mongo.db.listings
#     listings_data = scrape.scrape()
#     listings.update({}, listings_data, upsert=True)
#     return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
