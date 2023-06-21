def diff(Options, Options_eliminated):
    return (list(list(set(Options ) -set(Options_eliminated)) + list(set(Options_eliminated ) -set(Options))))

"""
   Import random - will be used to generate our random winning number

"""
import random


"""
   Options - the list of numbers from which users should select one, in an attempt to win the game

"""
Options = [1,2,3,4,5,6,7,8,9,10,11]

"""
   Options eliminaged - shows all the numbers already selected by the user

"""

Options_eliminated = []


"""
   Secret number - The range of numbers our algo will choose the winning number from

"""
secret_num = random.randint(1, 21)
print(secret_num)


"""
   Ask user for their name

"""
print("What is your name?")
my_name = input()


"""
   Ask user how much they would like to bet

"""

print("Hi " + my_name + ". How much would you like to wager? Your potential returns will win 10x your wager amount.")
bet_amount = int(input())
win_amount = str(bet_amount * int(10))

"""
   Thank the user and tell them how much they stand to win. 
   Importantly, their payout is slightly less than the probability 
   of them picking the correct number,    therefore creating a 
   house edge so that the game operator can profit from running the game,.

"""
print("Thanks " + my_name +". If you pick the correct number you will win $" + win_amount +". Good Luck.")



guess = ""
guess_count = 0
guess_limit = 11
out_of_guesses = False

"""
   Algo for sorting the user selections and the remaining numbers to choose from

"""
while guess_count < guess_limit and guess != secret_num and guess_count != 11:
    print("Choose a number from the options below")
    print(diff(Options, Options_eliminated))
    print(Options_eliminated)
    guess = input()
    guess = int(guess)
    Options_eliminated.append(guess)
    guess_count = guess_count + 1


    if guess != secret_num and guess_count <= 11:
        print("Try again")



if guess != secret_num:
    print('Hard luck')
else:
    print("Nice Guess! " + my_name + " You win $" + win_amount)



"""
   Notes:
   We need to add:
   - an alert if the user selects a number they have already previously chosen
   - a way for them to restart the game
"""

"""
   Operational note: The attractiveness of the game is that if the user keeps guessing, 
   and paying for each guess, they will definitely eventually win.
   However, because the payout is a smaller multiple than the number of selection choices,
   the house will always win in the long run.
"""