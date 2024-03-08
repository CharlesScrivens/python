# Practice with Lists in Python

# Creation
names = ["Peter", "Yuliana", "Valeria"]
print(names)
print(type(names))

# print data list
myData = ["Luisa", 37, "Imalvarez33@eafit.edu.co", 164.1]
print(myData)
for data in myData:
    print(type(data))
    print(data)
print(len(myData))

singers = ["Shakira", "Karol G", "Feid", "Maluma"]
singer1 = singers[0]

print(len(singers))
print(singer1)
print(singers[2])
print(singers[len(singers)-1])

motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles[0])

motorcycles[0] = "Ducati"
print(motorcycles[0])

# modifying lists
aliens = []
aliens.append("E.T")
aliens.append("Goku")
aliens.append("Marvin")
aliens.append("Gazoo")
print(aliens[1])
aliens.pop(1)
print(aliens[1])
print(aliens)

aliens.append("Goku")
i = 0
while(i < len(aliens)):
    print(aliens[i])
    i = i+1


colors = ["Yellow", "Blue", "Red"]
print(colors[len(colors)-1])

secretMessage = ["Planet", "You", "Secret", "Are", "Zombie", "The", "Nuclear", "Alien"]
i = 1
while(i < len(secretMessage)):
    print(secretMessage[i])
    i = i+2
