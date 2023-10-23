# f = open('./data/poem.txt', mode='r')
# poem = f.read()
# f.close()

with open('./data/poem.txt') as f:
    # print(type(f))
    poem = f.read()

print(poem)

#-----------------------

oceans = [
"Pacific",
"Atlantic",
"Indian",
"Southern",
"Arctic"
]

with open("oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")

        # Autre possibilité
        # print(ocean, file=f)