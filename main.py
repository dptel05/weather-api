from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def weather(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze()

    # Divide the temperature by 10 to format it correctly with one decimal place
    temperature_formatted = temperature / 10.0

    return {
        "station": station,
        "date": date,
        "temperature": temperature_formatted
    }


if __name__ == "__main__":
    app.run(debug=True, port=5001)
