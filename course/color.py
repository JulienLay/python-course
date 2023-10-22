import random
from sty import fg

def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return [r, g, b]

def color():
    message = 'This is a message'
    tr = ''
    for letter in message:
        tr += fg(random_color_generator()[0], random_color_generator()[1], random_color_generator()[2]) + letter
    print(tr + fg(255,255,255) + ' ')

color()