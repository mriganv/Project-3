#listing dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import tablescrape

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


mongo.db.wage2020.drop()
# Pass connection to the pymongo instance.


@app.route("/")
def index():
    wage2020 = mongo.db.wage2020.find_one()
    return render_template("index.html", wage = wage2020)

@app.route("/scrape")
def scrape():
    wage_data = tablescrape.scrape()
    mongo.db.wage2020.update({}, wage_data, upsert = True)
    return redirect("/", code= 302)

if __name__ == "__main__":
    app.run(debug=True)