# practicing for (foreach) loops

# with lists
ages = [25,7,39]
for age in ages:
    print(age)
print("end of program")

# with strings
message = "Hi SpaceX"
for character in message:
    print(character)

# with dictionaries
cyclist = {
    'firstName':'Egan',
    'lastName':'Bernal',
    'team':'Ineos'
}

for key in cyclist:
    print(key + ":" + cyclist[key])

# with lists containing dictionaries
nightclub1 = {'name':'perro negro','location':'poblado'}
nightclub2 = {'name':'teatro victoria','location':'poblado'}

nightclubs = [nightclub1, nightclub2]
for nightclub in nightclubs:
    print(nightclub['name'] + " - " + nightclub['location'])
