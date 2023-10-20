import random

def shifumi():
    dic = ['r', 'p', 's']
    computer_points = 0
    human_points = 0
    computer_choice = dic[random.randint(0, 2)]

    print('First round !')
    human_choice = input('Choose rock, paper or scissor --> type r or p or s :\n')
    print('Computer choice : ' + computer_choice)
    print('Your choice : ' + human_choice + '\n')

    if(human_choice == dic[0]):
        if(computer_choice == dic[1]):
            computer_points += 1
        else :
            human_points += 1
    elif(human_choice == dic[1]):
        if(computer_choice == dic[2]):
            computer_points += 1
        else :
            human_points += 1
    elif(human_choice == dic[2]):
        if(computer_choice == dic[0]):
            computer_points += 1
        else :
            human_points += 1

    print(f'Score : Computer {computer_points} - {human_points} You \n')

    print('Second round !')
    human_choice = input('Choose rock, paper or scissor --> type r or p or s :\n')
    print('Computer choice : ' + computer_choice)
    print('Your choice : ' + human_choice)

    if(human_choice == dic[0]):
        if(computer_choice == dic[1]):
            computer_points += 1
        else :
            human_points += 1
    elif(human_choice == dic[1]):
        if(computer_choice == dic[2]):
            computer_points += 1
        else :
            human_points += 1
    elif(human_choice == dic[2]):
        if(computer_choice == dic[0]):
            computer_points += 1
        else :
            human_points += 1

    print(f'Score : Computer {computer_points} - {human_points} You \n')

    if (computer_points == 2):
        print("You loose to the computer !")
        print(f'Computer points : {computer_points}')
        print(f'Human points : {human_points}')
    elif(human_points == 2) :
        print("You win !")
        print(f'Computer points : {computer_points}')
        print(f'Human points : {human_points}')
    else:
        print('Third round !')
        human_choice = input('Choose rock, paper or scissor --> type r or p or s :\n')
        print('Computer choice : ' + computer_choice)
        print('Your choice : ' + human_choice)

        if(human_choice == dic[0]):
            if(computer_choice == dic[1]):
                computer_points += 1
            else :
                human_points += 1
        elif(human_choice == dic[1]):
            if(computer_choice == dic[2]):
                computer_points += 1
            else :
                human_points += 1
        elif(human_choice == dic[2]):
            if(computer_choice == dic[0]):
                computer_points += 1
            else :
                human_points += 1

        if (computer_points == 2):
            print('-------------------')
            print("You loose to the computer !")
            print(f'Computer points : {computer_points}')
            print(f'Human points : {human_points}')
            print('-------------------')
        elif(human_points == 2) :
            print('-------------------')
            print("You win !")
            print(f'Computer points : {computer_points}')
            print(f'Human points : {human_points}')
            print('-------------------')
shifumi()