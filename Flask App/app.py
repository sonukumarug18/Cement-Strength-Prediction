from flask import Flask, render_template, url_for,request
import pickle as p
import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



modelfile = 'models/final_prediction.pickle'  
model = p.load(open(modelfile, 'rb'))
scaler= pickle.load(open('models/scaler.pickle','rb'))
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html') 

@app.route('/predict',methods =['GET','POST'])
def predict():
    Cement = float(request.form["Cement"])
    Blast_Furnace_Slag =float(request.form['Blast Furnace Slag'])
    Fly_Ash= float(request.form['Fly Ash'])
    Water=float(request.form['Water'])
    Superplasticizer = float(request.form['Superplasticizer'])
    Coarse_Aggregate  = float(request.form['Coarse Aggregate'])
    Fine_Aggregate= float(request.form['Fine Aggregate'])
    Age=float(request.form['Age'])


    total = [[Cement, Blast_Furnace_Slag, Fly_Ash, Water,Superplasticizer,Coarse_Aggregate,Fine_Aggregate,
               Age]]
    prediction = model.predict(scaler.transform(total))
    # prediction = int(prediction[0])


    return render_template('index.html',predict='The value predicted is {:.2f}'.format(prediction[0]))
   

    


if __name__ == '__main__':
    app.run(debug=True)
