import yfinance as yf
import time
import webbrowser
from flask import Flask, render_template, jsonify,request
price = ""

app = Flask(__name__)

@app.route("/data", methods=["GET","POST"])
def get_data():
    stock_name = yf.Ticker("RELIANCE.NS").info
    price = stock_name["regularMarketPrice"]
    print(price)
    return str(price)


@app.route("/", methods=["GET","POST"])
def stuff():
    
    return render_template("home.html")


app.run(debug=True)


