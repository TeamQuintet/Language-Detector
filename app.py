from flask import Flask, redirect, render_template, request, jsonify
from flask.helpers import make_response, url_for
import pandas as pd
# import tensorflow as tf
# import keras
# from keras.models import load_model


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index2.html")

# model = load_model('myModel.h5')

@app.route("/predict/", methods=["GET","POST"])
def predict():
    message = request.form['message']
    data = [message]
    # msg = toke
    prediction = 'English'
    return render_template("index2.html", prediction)

if __name__ == '__main__':
    app.run(debug=True)