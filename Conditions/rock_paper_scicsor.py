from random import randint

computer_choice = randint(1, 3)
user_choice = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 1 and computer_choice == 2:
    print("Computer wins! Paper covers Rock.")    
if user_choice == 1 and computer_choice == 3:
    print("You win! Rock smashes Scissors.")        
elif user_choice == 2 and computer_choice == 1:
    print("You win! Paper covers Rock.")    
elif user_choice == 2 and computer_choice == 3:
    print("Computer wins! Scissors cuts Paper.")    
elif user_choice == 3 and computer_choice == 1:
    print("Computer wins! Rock smashes Scissors.")    
elif user_choice == 3 and computer_choice == 2:
    print("You win! Scissors cuts Paper.")    
else:
    print("Invalid choice. Please select 1, 2, or 3.")    