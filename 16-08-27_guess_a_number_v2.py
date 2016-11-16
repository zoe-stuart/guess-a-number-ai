import random
import math


def start_screen():                                                          
    print("██████╗ ██████╗ ███████╗███████╗███████╗    ███████╗███╗   ██╗████████╗███████╗██████╗ ")
    print("██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝    ██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗")
    print("██████╔╝██████╔╝█████╗  ███████╗███████╗    █████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝")
    print("██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║    ██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗")
    print("██║     ██║  ██║███████╗███████║███████║    ███████╗██║ ╚████║   ██║   ███████╗██║  ██║")
    print("╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝")


def lose_screen():
    print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗")
    print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝")
    print(" ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  ")
    print("  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  ")
    print("   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗")
    print("   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝")


def win_screen():
    print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗")
    print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║")
    print(" ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║")
    print("  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║")
    print("   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║")
    print("   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝")


def end_screen():
    print(" ██████╗    ███═╗ ███╗     ███╗███████╗     ██████╗ ██╗     ██╗███████╗██████╗ ")
    print("██╔════╝   ██╔██╚╗████╗   ████║██╔════╝    ██╔═══██╗╚██╗   ██╔╝██╔════╝██╔══██╗")
    print("██║  ████╗██╔╝ ██║██╔██╗ ██╔██║█████╗      ██║   ██║ ╚██╗ ██╔╝ █████╗  ██████╔╝")
    print("██║    ██║███████║██║╚████╔╝██║██╔══╝      ██║   ██║  ╚████╔╝  ██╔══╝  ██╔══██╗")
    print("╚███████╔╝██║  ██║██║ ╚██╔╝ ██║███████╗    ╚██████╔╝   ╚██╔╝   ███████╗██║  ██║")
    print(" ╚══════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═╝╚══════╝     ╚═════╝     ╚═╝    ╚══════╝╚═╝  ╚═╝")

    
def play():

    low = 1
    high = 100
    limit = math.log(high - low, 2) + 1
    tries = 0

    print("Let's play a game!")
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".")
    print("You try to guess, and I'll tell you if you're right.")

    num = random.randint(1, 100)
    
    got_it = False

    while got_it == False and tries < limit:
        
        guess = input("What number am I thinking of? ")
        guess = int(guess)
        
        if guess < num:
            print("Nope. Your guess is too low.")
        elif guess > num:
            print("Nope. Your guess is too high.")
        else:
            got_it = True

        tries += 1

    if got_it == True:
        print("You guessed it!")
        win_screen()
    else:
        print("Sorry, that wasn't it.")
        lose_screen()


def play_again():

    while True:
        answer = input("Would you like to play again? ")

        if answer.lower() == 'no':
            return False   
        elif answer.lower() == 'yes':
            return True
        print("I don't understand. Please type yes or no.")



#game start
start_screen()

print("To begin the game.")
input()

again = True
    
while again == True:
    play()
    again = play_again()  

end_screen()
print("Thanks for playing!")








