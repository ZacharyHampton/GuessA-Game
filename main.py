import random

randomnum = random.randint(1, 100)  # Generates 'random' number
tries = 0  # Counter for number of tries
checknumber = False


def check(usernum):  # Function that takes the number, and gets if its out of range, equal to, lower, or higher than the random number. Also checks if not int.
    try: # Try to run the code
        usernum = int(usernum)  # Makes input to a string
        if (usernum > 100 or usernum < 1):  # If guess is above 100 or less than one, return out of range
            return "oor"
        if (usernum == randomnum):  # if guess is equal to random number, return True
            return True
        if (usernum > randomnum):  # If guess is greater than random number, return that our random number is lower
            return "Lower"
        if (usernum < randomnum):  # If guess is less than random number, return that our number is higher
            return "Higher"
    except (ValueError, TypeError):  # If there is a Value or Type error, return that the number isn't an integer
        return "NINT"


usernum = input("I am thinking of a number from 1 to 100, what is it? ")  # Asks user for a number
tries = tries + 1
checknumber = check(usernum)  # calls function with user input

while checknumber != True:  # While our input is not the random number
    if (checknumber == "Lower"):  # If function returns number is lower than randon number
        usernum = input("Our number is lower. What is it? ")  # Get new input
        tries = tries + 1  # Iterate tries +1
        checknumber = check(usernum)  # Check new input through function
    if (checknumber == "Higher"):  # If functions returns number is higher than random number
        usernum = input("Our number is higher. What is it? ")
        tries = tries + 1
        checknumber = check(usernum)
    if (checknumber == "oor"):  # If function returns that the input was out of range
        usernum = input(
            "That number is out of range. Remember, it is 1 to 100. Guess again! ")
        tries = tries + 1
        checknumber = check(usernum)
    if (checknumber == "NINT"):  # If function returns number is not an integer
        usernum = input("That number is not a number. Guess again! ")
        tries = tries + 1
        checknumber = check(usernum)
    if (checknumber == True):  # If function returns guess is equal to random number
        print("You found the number.")
        print(f"It took you {tries} tries to find the number.")
        # Tell user they found number and their tries.
