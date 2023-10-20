def average():
    cpt = 0
    grade = 0
    total = 0

    while(grade >= 0):
        grade = int(input('Type in your grade : '))
        if (grade >= 0):
            cpt +=1
            total += grade
        else:
            break
    if(cpt > 0):
        average = total/cpt
        print(f'The average of your {cpt} grades is {average}!')
    else:
        print('Not a number')

average()