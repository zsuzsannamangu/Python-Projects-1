#
# Python:   3.11.5
#
# Author:   Zsuzsanna Mangu
#
# Purpose:  The Tech Academy - Python Course, Creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#           Remember, function_name(variable) _means that we pass in the variable.
#           Return variable _means that we are returning the variable to
#           back to the calling function.


#adding default values to the variables, the parameters of start function:

def start(nice=0,mean=0,name=""):
    # get user's name:
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    
    """
        check if this is a new game or not,
        if it is new, get the user's name,
        if it is not a new game, thank the player for playing again
        and continue with the game
    """

    # meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name

    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        #we create a boolean variable that is named stop, and we say, while stop is True
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice or \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and stormes off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the 3 variables to the score()
            

def show_score(nice,mean,name):
    print("\n{}, your current score is: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    # the score function is being passed the values stored within the 3 variables
    if nice > 2: #if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    #Substitute the {} wildcards with our variable values
    
    from PIL import Image
    img = Image.open("sampleimg.jpeg")
    img.show()
    
    print("\nNice job {}, you win! \nThanks for being nice.".format(name))
    # then we call the again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nAhh too bad, game over {}!".format(name))
    # then we call the again function and pass in our variables
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit() #quit() is a built-in function
        else:
            print("\nEnter (Y) for 'Yes', (N) for 'No':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable so that we don't have to ask their name again
    start(nice,mean,name)







    

if __name__ == "__main__":
    start()






