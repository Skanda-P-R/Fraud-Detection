# Fraud-Detection

This repo contains the model to detect Financial Fraud. The Neural Network model has been trained an 6 lakh records (1/4th of actual data) of Synthetic Data generated by this <a href="https://www.msc-les.org/proceedings/emss/2016/EMSS2016_249.pdf">research paper</a><br>
The model is 99.922% accurate in predicting if a certain case is fraudulent or not.<br>
## Steps to run the Application
1. Run this command in cmd:<br>```pip install -r requirements.txt```<br>This will install all the dependencies required to run this application.
2. Next run<br>```python server.py```<br>This starts a Flask Server to which you can send JSON requests to.<br>The JSON Request format is:<br>
```
{
"amount": 0.0,
"oldbalanceOrg": 0.0,
"newbalanceOrig": 0.0,
"CASH_OUT": 0.0,
"CASH_IN": 0.0,
"DEBIT": 0.0,
"PAYMENT": 0.0,
"TRANSFER": 0.0
}
```
<br>The URL to which you send POST request will be like this:<br> ```http://127.0.0.1:5000/predict```
<br>
<br>

Now you can build your custom Application or website, which sends POST request to the model, and sends the Responce back in JSON format. <br><br>
For example, I have made a sample Tkinter Application, which is used to predict Fraud, by sending POST Request to the Flask Server running in the background.
