import random

def more_or_less():
    difficulty = input('Choose the level : easy, medium or hard :\n')
    if (difficulty == 'easy'):
        solution = random.randint(0, 10)
    elif (difficulty == 'medium'):
        solution = random.randint(0, 100)
    elif (difficulty == 'hard'):
        solution = random.randint(0, 1000)
    else :
        print("You need to type easy, medium or hard !")
        print("You didn't type it right, choosing easy !")
        solution = random.randint(0, 10)
    number = int(input("Type your number : "))
    count = 0

    while (number != solution) :
        if (number>solution) :
            print('Your number is too high')
            number = int(input("Type your number : "))
        elif(number<solution) :
            print('Your number is too low')
            number = int(input("Type your number : "))
        count+=1

    print(f'You won in {count} tries !')

more_or_less()