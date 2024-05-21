from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.stock_predictor.pipeline.prediction import PredictionPipeline

app = Flask(__name__)


@app.route('/',methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/train',methods = ['GET'])
def training():
    os.system('python main.py')
    return "Training Succesful...."

@app.route('/predict',methods = ['POST'])
def predict():
    if request.method == 'POST':
        try:
            date = float(request.form['date'])
            open = float(request.form['open'])
            high = float(request.form['high'])
            low = float(request.form['low'])
            volume = float(request.form['volume'])
            # free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])

            data = [date, open, high, low, volume]
            data = np.array(data).reshape(1, 11)

            obj = PredictionPipeline()
            prediction = obj.predict(data)
#
            return render_template('result.html', prediction = str(prediction))
#
        except Exception as e:
            return "Error: " + str(e)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 8080, debug = True)
