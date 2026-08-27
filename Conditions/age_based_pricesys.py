Age = int(input("Enter your age: "))
if Age < 18:
    print("You are a minor. Ticket price is 200 rupees.")
elif Age >= 18 and Age < 30:
    print("You are a young adult. Ticket price is 300 rupees.")
elif Age >= 30 and Age < 50:
    print("You are an adult. Ticket price is 400 rupees.")
else:
    print("You are a senior citizen. Ticket price is free.")