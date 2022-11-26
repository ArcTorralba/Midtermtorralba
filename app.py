from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route("/home")
@app.route('/')

def main():
    return render_template("index.html")

if __name__ == 'main':
    app.run()