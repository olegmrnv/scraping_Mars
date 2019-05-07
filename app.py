from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_info")

@app.route("/scrape")
def scrape():
    import scrape_mars
    data = scrape_mars.scrape()
    mars_collection = mongo.db.mars_collection
    mars_collection.update({}, data, upsert=True)
    db_data = mongo.db.mars_collection.find_one()
    
    return render_template("scrape.html", db_data = db_data)

@app.route("/")
def home():
    db_data = mongo.db.mars_collection.find_one()
    return render_template("index.html", db_data = db_data)

if __name__ == "__main__":
    app.run(debug=True)