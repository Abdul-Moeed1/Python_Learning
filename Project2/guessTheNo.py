import random

selectedNo = random.randint(1, 100)
print("Welcome to the Guess the Number Game!\nI have selected a number between 1 and 100. Try to guess it!")
attempts = 10

while (attempts > 0):
    guess  = int(input("Enter your guess: "))
    if(guess == selectedNo):
        print("You guessed it right! Congratulations!. Your score is: " + str(attempts))
        break
    elif(guess < selectedNo):
        print("Your guess is too low. Try again.")
        attempts -= 1
    else:
        print("Your guess is too high. Try again.")
        attempts -= 1
else:
    print("Sorry, you've run out of attempts. The number was: " + str(selectedNo))
    