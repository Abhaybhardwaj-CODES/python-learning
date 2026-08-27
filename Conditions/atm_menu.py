print("===== ATM MENU =====")
print("1. Check Balance")
print("2. Withdraw Money")
print("3. Deposit Money")
print("4. Exit")


choice = int(input("Enter your choice: "))
if choice == 1:
    balance = 1000  # Example balance
    print(f"Your current balance is: ₹{balance}")
elif choice == 2:
    withdraw_amount = int(input("Enter the amount to withdraw: "))
    balance = 1000  # Example balance
    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print(f"Withdrawal successful! Your new balance is: ₹{balance}")
    else:
        print("Insufficient balance.")
elif choice == 3:
    deposit_amount = int(input("Enter the amount to deposit: "))
    balance = 1000  # Example balance
    balance += deposit_amount
    print(f"Deposit successful! Your new balance is: ₹{balance}")
elif choice == 4:   
    print("Thank you for using the ATM. Goodbye!")        
