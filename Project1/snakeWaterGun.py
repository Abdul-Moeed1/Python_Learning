import random


def snakeWaterGun():
    options = ["s" , "w", "g"]
    valuesNames = {"s": "snake", "w": "water", "g": "gun"}
    userInput = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
    if userInput not in options:
        print("Invalid input. Please choose 's', 'w', or 'g'.")

    computerNum = random.randint(0,2)
    computerInput = options[computerNum]

    if userInput == computerInput:
        print(f"Both chose {valuesNames[userInput]}. It's a tie!")
        return "tie"
    elif (userInput == "s" and computerInput == "w") or (userInput == "w" and computerInput == "g") or (userInput == "g" and computerInput == "s"):
        print(f"You chose {valuesNames[userInput]} and computer chose {valuesNames[computerInput]}. You win!")
        return "user"
    else:
        print(f"You chose {valuesNames[userInput]} and computer chose {valuesNames[computerInput]}. Computer wins!")
        return "computer"



noOfMatches = int(input("Enter the number of matches you want to play: "))
compScore = 0
userScore = 0

for match in range(noOfMatches):
    print(f"\nMatch {match + 1}:")
    result = snakeWaterGun()
    if result == "tie":
        pass
    elif result == "user":
        userScore += 1
    else:
        compScore += 1
    print(f"Current Score - You: {userScore}, Computer: {compScore}")

if userScore > compScore:
    print(f"\nCongratulations! You won the series with a score of {userScore} to {compScore}.")
elif userScore < compScore:
    print(f"\nComputer won the series with a score of {compScore} to {userScore}. Better luck next time!")
else:
    print(f"\nThe series ended in a tie with both scoring {userScore}.")