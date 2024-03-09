# Dictionaries practice
product = {
    "name": "iPhone 14",
    "price": 799,
    "color": "midnight"
}

print(product)
print(type(product))

# lists are best used for storing ordered data of the same time
# dictionary best used for storing data where the order isn't important

computer = {"brand":"Dell", "processor":"i7"}
character = {"name":"Magician", "attack":20}
country = {"name":"Colombia", "capitalCity":"Bogeta"}

print(computer)
print(character)
print(country)

car = {'brand':'Toyota', 'color':'Black'}

print(len(car))
print(car['brand'])
print(car['color'])

car['color'] = 'Red'
print(car['color'])

car['cargoBox'] = 'SkyBox 16'
car['fender'] = 'Pocket style'
print(car['cargoBox'])
print(car)

car.pop("cargoBox")
print(car)

#list of products
product1 = {"name":"Monitor", "price":119}
product2 = {"name":"Mouse", "price":6}
productList = []
productList.append(product1)
productList.append(product2)

print(productList)
print(productList[0])
print(productList[0]['name'])

i = 0
while(i < len(productList)):
    print("Product name: " + productList[i]['name'])
    print("Product price: " + str(productList[i]['price']))
    i = i+1
