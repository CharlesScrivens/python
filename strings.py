# practice messing with strings
firstName = "John"
lastName = "Snow"
fullName = firstName + " " + lastName

print(fullName)
print("30 years old")
print(type(fullName))

message = "A Good Day!"
char0 = message[0]
char4 = message[4]
charLast = message[len(message)-1]

print(char0)
print(char4)
print(charLast)

subString1 = message[0:6]
subString2 = message[6:8]
print(subString1)
print(subString2)

indexO = message.find("o")
indexGood = message.find("Good")
indexZ = message.find("Z")

print(indexO)
print(indexGood)
print(indexZ)


product = "Laser-100-20"
indexDash1 = product.find("-")
indexDash2 = product.find("-", indexDash1 + 1)
subStringQuantity = product[indexDash2 + 1:len(product)]

print(indexDash1)
print(indexDash2)
print(subStringQuantity)

message2 = "Location: Provenza"

messageLower = message2.lower() # returns lowercase
print(messageLower)

messageUpper = message2.upper()
print(messageUpper)

countA = message2.count("a") #returns number of 'a' in message2
print(countA)

newMessage = message2.replace("a","x") #returns string with x in place of a
print(newMessage)

word = input("Enter a word: ")

i = 0
while(i < len(word)):
    print(word[i])
    i = i+1

text = "Ginza"
print(text[0])
print(text[0:3])
indexZ = text.find("z")
print(indexZ)
