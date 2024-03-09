# practice with functions
def greet():
    print("Welcome")
    print("To my program")

def customGreeting(firstName, lastName):
    print(f'Hello {firstName} {lastName}')

customGreeting('Sinan', 'Boo')
customGreeting('Choi', 'Kimukimu')


greet()
print("EoP")

def calculateFine(daysLate):
    if(daysLate>7):
        return daysLate*2
    else:
        return 3

days = int(input('Enter the num days late: '))
fine = calculateFine(days)
print('You must pay a fine of ' + str(fine) + ' dollars')

def printFirstName(names):
    for name in names:
        print(name)

gods = ['Zeus','Poseidon','Anubis']
printFirstName(gods)


