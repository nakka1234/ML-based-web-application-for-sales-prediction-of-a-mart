from flask import Flask,jsonify,render_template,request
import joblib
import os
import numpy as np


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")
@app.route('/predict',methods=['POST'])
def result():
    Item_Weight=float(request.form['Item_Weight'])
    Item_Fat_Content = float(request.form['Item_Fat_Content'])
    Item_Type= float(request.form['Item_Type'])
    Item_MRP = float(request.form['Item_MRP'])
    Outlet_Size= float(request.form['Outlet_Size'])
    Outlet_Location_Type = float(request.form['Outlet_Location_Type'])
    Outlet_Type = float(request.form['Outlet_Type'])
    x=np.array([[Item_Weight,Item_Fat_Content,Item_Type,Item_MRP,Outlet_Size,Outlet_Location_Type,Outlet_Type]])
    scaler_path=os.path.join(r'C:\Users\N.Srinivas\Desktop\Sales prediction ml project\model\sc.sav')
    sc=joblib.load(scaler_path)
    x_std=sc.transform(x)
    model_path=r'C:\Users\N.Srinivas\Desktop\Sales prediction ml project\model\grid_search.sav'
    model=joblib.load(model_path)
    output= model.predict(x_std)
    return render_template('home.html',prediction_text='Expected Sales{}'.format(output))

if __name__=="__main__":
    app.run(debug=True,port=9457)