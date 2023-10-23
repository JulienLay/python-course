def cesar(number):
    message = "this is a test !"
    tr = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alphabet_changed = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for i in range(number):
        first_character = alphabet_changed.pop(0)
        alphabet_changed.append(first_character)

    for letter in message:
        try :
            index_alphabet = alphabet.index(letter.lower())
        except Exception:
            tr += letter
        else :
            letter_alphabet_changed = alphabet_changed[index_alphabet]
            tr += letter_alphabet_changed
    return tr