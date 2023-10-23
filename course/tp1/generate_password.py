import random
import string
import time

def generate_password(length_of_password):
    uppercases = string.ascii_uppercase
    lowercases = string.ascii_lowercase
    digits = string.digits
    special_characters = '()[]:;!'
    possible_characters = uppercases + lowercases + digits + special_characters
    password = ''

    for _ in range(length_of_password):
        password += random.choice(possible_characters)

    return password

def bruteforce(target_password):
    length_of_password = len(target_password)
    uppercases = string.ascii_uppercase
    lowercases = string.ascii_lowercase
    digits = string.digits
    special_characters = '()[]:;!'
    possible_characters = uppercases + lowercases + digits + special_characters
    answer = ''
    count = 0

    for i in range(length_of_password):
        for j in range(len(possible_characters)):
            if possible_characters[j] == target_password[i]:
                answer += possible_characters[j]
                print(f"Tryn number {count}: {answer}")
            count += 1

    print(f'This is the found password with bruteforce : {answer}')
    print(f"Total number of tries : {count}")

generated_password = generate_password(6)
print(f'This is the generate password : {generated_password}')
found_password = bruteforce(generated_password)

# Mesure time execution with bruteforce
start_time = time.time()
found_password = bruteforce(generated_password)
end_time = time.time()

print(f'Time taken for bruteforce: {end_time - start_time} seconds')

# Majuscules : Il y a 26 lettres majuscules de l'alphabet anglais (A-Z).
# Minuscules : Il y a 26 lettres minuscules de l'alphabet anglais (a-z).
# Chiffres : Il y a 10 chiffres possibles (0-9).
# Caractères spéciaux : Il y a 7 caractères spéciaux possibles ('(', ')', '[', ']', ':', ';', '!').

# Pour chaque position du mot de passe, il y a 26 (majuscules) + 26 (minuscules) + 10 (chiffres) + 7 (caractères spéciaux) options possibles. Donc, le nombre total de combinaisons possibles pour un mot de passe de 6 caractères est :
# Nombre de combinaisons = (26 + 26 + 10 + 7)^6

# Calculons le résultat :
# Nombre de combinaisons = (69)^6 ≈ 193,514,172,349,224 combinaisons possibles.

# Il y a environ 193,514 milliards de combinaisons possibles pour un mot de passe de 6 caractères composé de majuscules, minuscules, chiffres et les caractères spéciaux mentionnés.