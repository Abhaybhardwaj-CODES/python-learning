print("===== RESTAURANT MENU =====")
print("1. Pizza - ₹200")
print("2. Burger - ₹100")
print("3. Pasta - ₹150")
print("4. Coke - ₹50")

choice = int(input("Enter your choice: "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    item = "Pizza"
    total_price = 200 * quantity
    print(f"Total price for {quantity} Pizza(s): ₹{total_price}")   
elif choice == 2:
    item = "Burger"
    total_price = 100 * quantity
    print(f"Total price for {quantity} Burger(s): ₹{total_price}")
elif choice == 3: 
    item = "Pasta"      
    total_price = 150 * quantity
    print(f"Total price for {quantity} Pasta(s): ₹{total_price}")
elif choice == 4:
    item = "Coke"
    total_price = 50 * quantity
    print(f"Total price for {quantity} Coke(s): ₹{total_price}")
else:
    print("Invalid choice. Please select a valid menu item.")   