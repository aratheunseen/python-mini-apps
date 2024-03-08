from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data-small/stations.txt",skiprows=17)

@app.route("/")
def home():
    return render_template("home.html",data=stations[["STAID","STANAME                                 "]].to_html())

@app.route("/api/v1/<station>")
def station_wise_weather_report(station):
    filepath = "data-small/TG_STAID" + str(station).zfill(6) +".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient="records")
    return result

@app.route("/api/v1/annual/<station>/<year>")
def year_wise_weather_report(station, year):
    filepath = "data-small/TG_STAID" + str(station).zfill(6) +".txt"
    df = pd.read_csv(filepath, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient="records")
    return result

@app.route("/api/v1/<station>/<date>")
def weather_report(station, date):
    filepath = "data-small/TG_STAID" + str(station).zfill(6) +".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    result = {
        "station": station,
        "date": date,
        "temperature": temperature
    }
    return result

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)