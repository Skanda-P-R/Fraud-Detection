from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import pandas as pd

model = load_model('Financial_Fraud_Detection_Model.h5')

server = Flask(__name__)

@server.route('/predict', methods=['POST'])
def predict():
    data = request.get_json() 

    features = (
        data.get('amount', 0.0),
        data.get('oldbalanceOrg', 0.0),
        data.get('newbalanceOrig', 0.0),
        data.get('CASH_OUT', 0.0),
        data.get('CASH_IN', 0.0),
        data.get('DEBIT', 0.0),
        data.get('PAYMENT', 0.0),
        data.get('TRANSFER', 0.0)
    )
    test_pd = pd.DataFrame([features], columns=["amount", "oldbalanceOrg", "newbalanceOrig", "CASH_OUT", "CASH_IN", "DEBIT", "PAYMENT", "TRANSFER"])

    y_pred = model.predict(test_pd)

    if(y_pred[0][0] == 1.0):
        pred = True
    else:
        pred = False
    
    return jsonify({'prediction': pred})

if __name__ == '__main__':
    server.run(debug=True)
