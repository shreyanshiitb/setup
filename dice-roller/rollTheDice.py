import random
min, max = 1, 6
roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print(f'Rolling the dice.... Number is {random.randint(min, max)}')

    roll_again = input("Do you want to roll again?")

print('Sad to see you go. Come back soon!!')
