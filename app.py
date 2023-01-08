import pickle
from flask import Flask,request

model=pickle.load(open('model.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def homepage():
    return 'API Server Launched'

@app.route('/predict',methods=['GET'])
def predict():
    type=float(request.args.get('type'))
    amount=float(request.args.get('amount'))
    oldbalance=float(request.args.get('oldbalance'))
    newbalance=float(request.args.get('newbalance'))
    data=[[type,amount,oldbalance,newbalance]]
    result=model.predict(data)[0]
    return result


if  __name__=="__main__":
    app.run(
        host='0.0.0.0',
        port=5001,
        debug=True
    )