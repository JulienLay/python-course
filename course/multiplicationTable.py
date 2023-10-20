def multiplication_table() :
    number = int(input('Type your multiplication table number : '))
    multiplication_table_list = []
    for i in range(1, 10):
        if ((number*i)%3 == 0) :
            multiplication_table_list.append(str(number*i)+'*')
        else :
            multiplication_table_list.append(number*i)
    print(multiplication_table_list)

multiplication_table()