class BankWithdrawalException(Exception):
    """Custom exception for bank withdrawal errors."""
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f"BankWithdrawalException: {self.message}"

withdrawal_amount = 1500
try:
    if withdrawal_amount > 1000:  # Assuming the account balance is 1000
        raise BankWithdrawalException("Insufficient funds for withdrawal.")
    else:
        print(f"Withdrew {withdrawal_amount} successfully.")
    
except BankWithdrawalException as e:
    print("Error:", e)