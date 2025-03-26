import requests

class Mpesa:
    def __init__(self):
        self.api_url = "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        self.headers = {
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",
            "Content-Type": "application/json"
        }
    
    def process_payment(self, transaction):
        payload = {
            "BusinessShortCode": "174379",
            "Password": "YOUR_PASSWORD",
            "Timestamp": "20250326214644",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": transaction['amount'],
            "PartyA": transaction['phone_number'],
            "PartyB": "174379",
            "PhoneNumber": transaction['phone_number'],
            "CallBackURL": "https://your_callback_url",
            "AccountReference": transaction['transaction_id'],
            "TransactionDesc": "Payment for goods"
        }
        
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        
        if response.status_code == 200:
            return True
        else:
            return False