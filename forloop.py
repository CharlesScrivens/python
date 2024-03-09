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

# range function (can have single number which it goes to, 2 numbers for start and [end-1] and 3 to have a counter
for number in range(6):
    print(number)

for number in range(1,7,2):
    print(number)

for number in range(1,81):
    print(number)

for number in range(1000,0,-100):
    print(number)

for number in range(2,68,2):
    print(number)

name1 = input("Enter name 1: ")
name2 = input("Enter name 2: ")
name3 = input("Enter name 3: ")
name4 = input("Enter name 4: ")

names = []
names.append(name1)
names.append(name2)
names.append(name3)
names.append(name4)

for name in names:
    if name[0] == "L" or name[0] == 'l':
        print("Name discarded")
    else:
        print(name)
