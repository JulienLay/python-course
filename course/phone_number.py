def phone_number():
    dic = {
        '0' : 'Zero',
        '1' : 'One',
        '2' : 'Two',
        '3' : 'Three',
        '4' : 'Four',
        '5' : 'Five',
        '6' : 'Six',
        '7' : 'Seven',
        '8' : 'Eight',
        '9' : 'Nine',
    }
    letter_phone_number = ''

    phone_number_input = input("Type in your phone number : ")
    for letter in phone_number_input :
        letter_phone_number += dic[letter] + " "

    print(letter_phone_number)

phone_number()