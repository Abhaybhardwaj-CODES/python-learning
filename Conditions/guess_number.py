from random import randint
chances = 5


user_guess = int(input("Guess a number between 1 and 100: "))
computer_number = randint(1, 100)

if chances > 0:
    print(f"You have {chances} chances to guess the number.")

    
    
while  user_guess < computer_number:
    print("Your guess is too low. Try again and guess higher.")
    user_guess = int(input("Guess a number between 1 and 100: "))
    chances -= 1
print(f"You have {chances} chances left.")    
while user_guess > computer_number:
    print("Your guess is too high. Try again and guess lower.")
    user_guess = int(input("Guess a number between 1 and 100: "))
    chances -= 1
    print(f"You have {chances} chances left.")    
if user_guess == computer_number:
    print(f"Congratulations! You guessed {user_guess} which is correct.")
    print(f"You guessed the number in {5 - chances} chances.")

elif chances == 0:
    print("Sorry, you have used all your chances.")    

    
else:
    print(f"Sorry, the number was {computer_number}. Better luck next time!")
        