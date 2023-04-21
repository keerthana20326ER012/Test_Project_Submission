#importing the necessary dependencies 
from flask import flask,request,render_template
import numpy as np
import pandas as pd
import pickle
import os


model = pickle.load(open('flight.pk1',rb'))
app=flask(_name_)#initializing the app


@app.route('/')
]def home():
      return render_template("index.html")

@app.route('/prediction'.methods =['POST']0


def predict():
name = request.from['name']
month = request.from['month']
daypfmonth = request.from['dayofmonth
dayofweek = request.from['dayofweek']
origin = request.from['origin']
if(origin == "msp"):
    origin1,origin2,origin3,origin4,origin5 = 0,0,0,0,1
if(origin == "dtw"):
    origin1,origin2,origin3,origin4,origin5 = 1,0,0,0,0
if(origin == "jfk"):
    origin1,origin2,origin3,origin4,origin5 = 0,0,1,0,0
if(origin == "sea"):
    origin1,origin2,origin3,origin4,origin5 = 0,1,0,0,0
if(origin == "alt"):
    origin1,origin2,origin3,origin4,origin5 = 0,0,0,1,0


destination = request.from['destination']
if(destination == "msp"):
    destination1,destination2,destination3,distination4,distination5 = 0,0,0,0,1
if(destination == "dtw"):
    destination1,destination2,destination3,distination4,distination5 = 1,0,0,0,0
if(destination == "jfk"):
    destination1,destination2,destination3,distination4,distination5 = 0,0,1,0,0
if(destination == "sea"):
    destination1,destination2,destination3,distination4,distination5 = 0,1,0,0,0
if(destination == "alt"):
    destination1,destination2,destination3,distination4,distination5 = 0,0,0,1,0
dept=request.from['dept']
arrtime = request.from['arrtime']
actdept = request.from['actdept']
dept15=int(dept)-int(actdept)
total = [[name,month,dayofmonth,dayofweek,origin1,origin2,origin3,origin4,origin5,destinationa1,destination2,destination3,destination4,destination5
#print(total)
print(y_pred)
if(y_pred==[0,]):
    ans="The Flight wil be on time"
else:
   ans="the Flight will be delayed"
return render_template("index.html",showcase = ans)


if_name_ == '_main_':
   app.run(debug = ture)


