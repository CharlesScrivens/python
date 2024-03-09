# more practice
file = open('customers.txt')
content = file.readlines()
print(content)

for line in content:
    line = line.strip() #removes leading/trailing whitespace
    customerData = line.split(',')
    print('First Name: ' + customerData[0])
    print('Last Name: ' + customerData[1])
    print('Age: ' + customerData[2])


# saving to files
savingsFile = open('savings.txt')
content = savingsFile.read()

savingsFileW = open('savings.txt', 'w')
newSaving = input('enter your savings for the week: ')
newContent = content + ',' + newSaving

savingsFileW.write(newContent)
savingsFileW.close()
