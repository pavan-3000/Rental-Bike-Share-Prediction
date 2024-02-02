from flask import Flask,render_template,request
from src.mlproject.pipeline.predict import PredictionPipeline
import joblib
import os 
from pathlib import Path
import numpy as np 

app = Flask(__name__)


model = joblib.load(Path(os.path.join('artifacts/model_trainer/model.joblib')))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/train',methods=['GET'])
def train():
    os.system("python main.py")
    return "trianing is suscesssfuull"


@app.route('/predict',methods=['POST','GET'])
def predict():
     instant   = float(request.form['instant'])    
     season    = float(request.form['season'])
     yr        = float(request.form['yr'])
     mnth      = float(request.form['mnth'])
     hr        = float(request.form['hr'])
     holiday   = float(request.form['holiday'])
     weekday   = float(request.form['weekday'])
     workingday= float(request.form['workingday'])
     weathersit= float(request.form['weathersit'])
     temp      = float(request.form['temp'])
     atemp     = float(request.form['atemp'])
     hum       = float(request.form['hum'])
     windspeed = float(request.form['windspeed'])
     casual    = float(request.form['casual'])
     registered= float(request.form['registered'])
     
     
     data = [instant  ,
             season    ,
             yr        ,
             mnth      ,
             hr        ,
             holiday   ,
             weekday   ,
             workingday,
             weathersit,
             temp      ,
             atemp     ,
             hum       ,
             windspeed ,
             casual    ,
             registered]
     data = np.array(data).reshape(1,15)
     print(data)
     
     pre_obj = PredictionPipeline()
     
     prediciton = pre_obj.predict(data)
     return render_template('result.html',prediction=prediciton)
 
    
 
     
     
     
     
     
     


if __name__ == "__main__":
    app.run(debug=True)