import random

# r=random.randrange(-1 ,10) untuk random number kecuali 10
# r=random.randrint(-1 ,10)untuk random number termasuk 10

top_of_range = input('type a number: ')
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)

while True:
    user_guess = input("make a guess: ")
    if user_guess.isdigit():  # Added parentheses after isdigit
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print('you got it')
        break
    else:
        print('you got it wrong')