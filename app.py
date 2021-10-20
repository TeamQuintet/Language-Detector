from flask import Flask, redirect, render_template, request, jsonify
from flask.helpers import make_response, url_for
# import pandas as pd
# import tensorflow as tf
# import keras
# from keras.models import load_model


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# model = load_model('myModel.h5')

@app.route("/detect", methods=["GET", "POST"])
def predictor():
    return render_template("detect.html")

@app.route("/translate", methods=["GET", "POST"])
def translator():
    return render_template("translate.html")

if __name__ == '__main__':
    app.run(debug=True)