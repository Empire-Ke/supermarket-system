from mpesa import Mpesa
from receipt import generate_receipt

def main():
    # Simulate receiving a transaction
    transaction = {
        'amount': 1000,
        'phone_number': '254712345678',
        'transaction_id': 'TX123456'
    }
    
    # Process Mpesa payment
    mpesa = Mpesa()
    if mpesa.process_payment(transaction):
        # Generate receipt
        receipt = generate_receipt(transaction)
        print(receipt)
    else:
        print("Payment failed.")

if __name__ == "__main__":
    main()