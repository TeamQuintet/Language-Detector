from flask import Flask, redirect, render_template, request, jsonify
from flask.helpers import make_response, url_for
from extract import extractFromFile

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

@app.route("/upload", methods=["GET", "POST"])
def upload():
    imagefile = request.files.get('imagefile', '')
    text = extractFromFile()
    return render_template("detect.html", content=text)

if __name__ == '__main__':
    app.run(debug=True)