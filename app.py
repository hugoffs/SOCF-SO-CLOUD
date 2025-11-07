from flask import Flask, render_template
import platform
import psutil
import os 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/metricas")
def metricas():
    return render_template("metricas.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
