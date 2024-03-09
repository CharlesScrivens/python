# practice with pyplot
import matplotlib.pyplot as plt

# x represents years
x = [2012,2013,2014,2015,2016,2017]
# y reps amnt money saved
y = [0,50,70,70,100,246]

plt.plot(x,y)
plt.xlabel('year')
plt.ylabel('savings (usd)')
plt.show()
