# practice with counters, accumulators, and flags

ages = [34, 50, 28, 20, 44]
counterOver30 = 0
for age in ages:
    if (age > 30):
        counterOver30 = counterOver30 + 1

print(f'total over 30: {counterOver30}')

city1 = {'name':'Envigado','population': 249800}
city2 = {'name':'San Diego','population': 1000000}
city3 = {'name':'Chula Vista','population': 87000}

cities = [city1,city2,city3]
count = 0
popAcc = 0
for city in cities:
    if(city['population'] > 90000):
        count = count+1
    popAcc = popAcc + city['population']

print(f'population over 90000: {count}')
average = popAcc/len(cities)
print(f'average population: {average}')


salaries = [3000, 1500, 800]

salaryAcc = 0
i = 0
while(i < len(salaries)):
    salaryAcc = salaryAcc + salaries[i]
    i = i+1

print(f'totaly salary sum: {salaryAcc}')


# grade exercise
grades = [4.0,2.0,1.2,4.7,1.7]
highGradeFlag = False 

for grade in grades:
    if(grade>4.5):
        highGradeFlag = True
        break

if(highGradeFlag):
    print('you have at least one high grade')
else:
    print('you did not obtain the high grade')

