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


from datetime import datetime


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            date_str = request.form['date']
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            date_num = (date_obj - datetime(1970, 1, 1)).days

            open = float(request.form['open'])
            high = float(request.form['high'])
            low = float(request.form['low'])
            volume = float(request.form['volume'])
            dividend = float(request.form['dividend'])
            stock_split = float(request.form['stock_split'])

            data = [date_num, open, high, low, volume, dividend, stock_split]
            data = np.array(data).reshape(1, -1)  # Adjust the reshape parameters according to your model's input shape

            obj = PredictionPipeline()
            prediction = obj.predict(data)

            return render_template('result.html', prediction=str(prediction))

        except Exception as e:
            return "Error: " + str(e)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 8080, debug = True)
