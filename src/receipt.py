import datetime

def generate_receipt(transaction):
    receipt = f"""
    Receipt
    --------------------
    Transaction ID: {transaction['transaction_id']}
    Amount: {transaction['amount']}
    Phone Number: {transaction['phone_number']}
    Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    --------------------
    Thank you for your purchase!
    """
    return receipt