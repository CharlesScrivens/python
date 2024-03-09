# more practice with functions
def add():
    num1 = float(input('enter first num: '))
    num2 = float(input('enter second num: '))
    result = num1 + num2
    print(f'result is: {result}')

def subtract():
    num1 = float(input('enter first num: '))
    num2 = float(input('enter second num: '))
    result = num1 - num2
    print(f'result is: {result}')

def multiply():
    num1 = float(input('enter first num: '))
    num2 = float(input('enter second num: '))
    result = num1 * num2
    print(f'result is: {result}')

def divide():
    num1 = float(input('enter first num: '))
    num2 = float(input('enter second num: '))
    result = num1 / num2
    print(f'result is: {result}')

while(True):
    print('-----Enter the operation----')
    print('0) Exit')
    print('1) Add')
    print('2) Subtract')
    print('3) Multiply')
    print('4) Divide')

    operation = int(input())
    if(operation == 0):
        print('byeeee')
        break
    elif(operation == 1):
        add()
    elif(operation == 2):
        subtract()
    elif(operation == 3):
        multiply()
    elif(operation == 4):
        divide()
    else:
        print('select a correct choice')
