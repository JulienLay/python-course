def count_letters():
    text = 'Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth.'
    dic = {}
    for letter in text :
        dic[letter] = text.count(letter)
    print(dic)

count_letters()