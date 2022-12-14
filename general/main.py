
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/data", methods=["GET","POST"])
def get_data():
    #RUN YOUR API OR FUNCTION HERE
    return #your data# #pro tip: make sure its in string format#


@app.route("/", methods=["GET","POST"])
def home():
 
    return render_template("main.html")


app.run(debug=True)

