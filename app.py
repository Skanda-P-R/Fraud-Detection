import tkinter as tk
import requests
import json

def send_request():
    data = {
        'amount': float(amount_entry.get()),
        'oldbalanceOrg': float(oldbalanceOrg_entry.get()),
        'newbalanceOrig': float(newbalanceOrig_entry.get()),
        'CASH_OUT': float(cash_out_entry.get()),
        'CASH_IN': float(cash_in_entry.get()),
        'DEBIT': float(debit_entry.get()),
        'PAYMENT': float(payment_entry.get()),
        'TRANSFER': float(transfer_entry.get())
    }
    
    response = requests.post('http://127.0.0.1:5000/predict', json=data)
    result = response.json().get('prediction')
    result_label.config(text=f'Prediction: {"Fraud" if result else "Not Fraud"}')

root = tk.Tk()
root.title('Fraud Detection')

tk.Label(root, text='Amount').grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text='Old Balance Original').grid(row=1, column=0)
oldbalanceOrg_entry = tk.Entry(root)
oldbalanceOrg_entry.grid(row=1, column=1)

tk.Label(root, text='New Balance Original').grid(row=2, column=0)
newbalanceOrig_entry = tk.Entry(root)
newbalanceOrig_entry.grid(row=2, column=1)

tk.Label(root, text='CASH_OUT').grid(row=3, column=0)
cash_out_entry = tk.Entry(root)
cash_out_entry.grid(row=3, column=1)

tk.Label(root, text='CASH_IN').grid(row=4, column=0)
cash_in_entry = tk.Entry(root)
cash_in_entry.grid(row=4, column=1)

tk.Label(root, text='DEBIT').grid(row=5, column=0)
debit_entry = tk.Entry(root)
debit_entry.grid(row=5, column=1)

tk.Label(root, text='PAYMENT').grid(row=6, column=0)
payment_entry = tk.Entry(root)
payment_entry.grid(row=6, column=1)

tk.Label(root, text='TRANSFER').grid(row=7, column=0)
transfer_entry = tk.Entry(root)
transfer_entry.grid(row=7, column=1)

predict_button = tk.Button(root, text='Predict', command=send_request)
predict_button.grid(row=8, column=0, columnspan=2)

result_label = tk.Label(root, text='Prediction: ')
result_label.grid(row=9, column=0, columnspan=2)

root.mainloop()
