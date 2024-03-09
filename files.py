# practice with files

# open file
savingsFile = open('savings.txt')
content = savingsFile.read()
savings = content.split(',')


print(savings)
print(len(savings))
print(savings[0])
print(content)
