def diff(Options, Options_eliminated):
    return (list(list(set(Options ) -set(Options_eliminated)) + list(set(Options_eliminated ) -set(Options))))


import random

Options = [1,2,3,4,5,6,7,8,9,10,11]

Options_eliminated = []


secret_num = random.randint(1, 21)
print(secret_num)

print("What is your name?")
my_name = input()


print("Hi " + my_name + ". How much would you like to wager? Your potential returns will win 10x your wager amount.")
bet_amount = int(input())
win_amount = str(bet_amount * int(10))

print("Thanks " + my_name +". If you pick the correct number you will win $" + win_amount +". Good Luck.")



guess = ""
guess_count = 0
guess_limit = 11
out_of_guesses = False


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



