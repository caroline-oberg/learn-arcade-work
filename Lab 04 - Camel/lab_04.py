# Lab 04 Camel Game
import random

def main():

    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi dessert.")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the natives.")

    done = False
    milesTraveled = 0
    nativesTraveled = -20
    camelTiredness = 0
    thirst = 0
    canteen = 3

    while not done:
        print()
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print()
        userInput = input("What will you do? ")
        print()
        if userInput.upper() == "Q" :
            done = True

        # Status Check.
        elif userInput.upper() == "E" :
            print("Miles traveled:", milesTraveled)
            print("Drinks in canteen:", canteen)
            print("The natives are", milesTraveled - nativesTraveled, "miles behind you.")

        # Stop for the night.
        elif userInput.upper() == "D" :
            print("You stop for the night.")
            print("Your camel is happy.")
            print("The natives don't stop.")
            camelTiredness = 0
            nativesTraveled += random.randrange(7, 15)

        # Ahead full speed.
        elif userInput.upper() == "C" :
            miles = random.randrange(10, 21)
            milesTraveled += miles
            thirst += 1
            camelTiredness += random.randrange(1,4)
            nativesTraveled += random.randrange(7, 15)
            print("You push onward at full speed, moving a total of", miles, "miles.")
            print("Your thirst increases.")
            print("Your camel grows tired.")
            print("The natives continue the chase.")

        # Ahead moderate speed.
        elif userInput.upper() == "B" :
            miles = random.randrange(5, 13)
            milesTraveled += miles
            thirst += 1
            camelTiredness += 1
            nativesTraveled += random.randrange(7, 15)
            print("You move forward, moving a total of", miles, "miles.")
            print("Your thirst increases.")
            print("The natives continue the chase.")

        # Drink from your canteen.
        elif userInput.upper() == "A":
            if canteen > 0 :
                canteen -= 1
                thirst = 0
                print("You take a drink.")
            else:
                print("Your canteen is empty.")

        if thirst > 5:
            print("You died of thirst!")
            print("Game Over.")
            done = True
        elif thirst > 4:
            print("You are thirsty.")

        if not done and milesTraveled >= 200:
            print("Congratulations! You have crossed the desert!")
            print("You win!")
            done = True

        if not done and camelTiredness > 8:
            print("Your camel died of exhuastion!")
            print("With no camel, the natives catch up to you.")
            print("Game over.")
            done = True
        elif camelTiredness > 5:
            print("Your camel is tired.")

        if not done and milesTraveled - nativesTraveled <= 0:
            print("The natives have caught up with you!")
            print("Game over.")
        elif milesTraveled - nativesTraveled < 15:
            print("You see faint shapes on the horizon behind you. ")
            print("The natives are getting close!")

main()