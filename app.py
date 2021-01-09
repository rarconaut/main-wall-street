#################################################
# Main-Wall-Street UCSD Data Science & Viz Bootcamp
# Project 2 Group 6 Bretton, Brice, Gunjan, Jeremy, Rawaf
#################################################


#################################################
# Dependencies (from Lesson 10 Activity 10-Ins_Flask_with_ORM)
#################################################
from flask import make_response, redirect, render_template, request, url_for
from flask import current_app as app

import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
# engine = create_engine("postgresql://postgres:postgres@localhost/project_2_corp_capital")

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)

# # Save reference to the table
# Data = Base.classes.combined_data


#################################################
# Flask Setup
#################################################
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/project_2_corp_capital"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


"""Data models."""
class Data(db.Model):
    __tablename__ = "combined_data"

    ticker = db.Column(db.Unicode, primary_key=True)
    exchange = db.Column(db.Unicode)
    sector = db.Column(db.Unicode)
    industry = db.Column(db.Unicode)
    state_val = db.Column(db.Unicode)
    city = db.Column(db.Unicode)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    rpt_year = db.Column(db.Unicode)
    revenue_scaled = db.Column(db.Integer)
    income_tax_scaled = db.Column(db.Integer)
    net_income_scaled = db.Column(db.Integer)
    market_cap = db.Column(db.Integer)
    median_hh_income = db.Column(db.Integer)

    def __repr__(self):
        return "<Data {}>".format(self.data)



#################################################
# Flask Routes
#################################################


# Create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Create a different route for each element's API (built from querying our database)
# - these will be the source json URLs for our visualizations' .js files
@app.route("/api")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/combined-data<br/>"
    )

@app.route("/api/combined-data")
def combinedData():
    results = db.session.query(
        Data.ticker,
        Data.exchange,
        Data.sector,
        Data.industry,
        Data.state_val,
        Data.city,
        Data.lat,
        Data.lon,
        Data.rpt_year,
        Data.revenue_scaled,
        Data.income_tax_scaled,
        Data.net_income_scaled,
        Data.market_cap,
        Data.median_hh_income
    ).all()

    ticker = [result[0] for result in results]
    exchange = [result[1] for result in results]
    sector = [result[2] for result in results]
    industry = [result[3] for result in results]
    state = [result[4] for result in results]
    city = [result[5] for result in results]
    lat = [result[6] for result in results]
    lon = [result[7] for result in results]
    year = [result[8] for result in results]
    revenue = [result[9] for result in results]
    tax = [result[10] for result in results]
    net = [result[11] for result in results]
    cap = [result[12] for result in results]
    mhi = [result[13] for result in results]
  

    # Create a dictionary for each company (from the row data) and append to a list of all_passengers
    all_data = []
    for (
        ticker,
        exchange,
        sector,
        industry,
        state,
        city,
        lat,
        lon,
        year,
        revenue,
        tax,
        net,
        cap,
        mhi
        ) in results:
        combined_data = {}
        combined_data["ticker"] = ticker
        combined_data["exchange"] = exchange
        combined_data["sector"] = sector
        combined_data["industry"] = industry
        combined_data["state"] = state
        combined_data["city"] = city
        combined_data["lat"] = lat
        combined_data["lon"] = lon
        combined_data["report_year"] = year
        combined_data["revenue"] = revenue
        combined_data["income_tax"] = tax
        combined_data["net_income"] = net
        combined_data["market_cap"] = cap
        combined_data["median_hh_income"] = mhi
        all_data.append(combined_data)

    return jsonify(all_data)


if __name__ == '__main__':
    app.run(debug=True)
