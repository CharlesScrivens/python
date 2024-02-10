# Arrays (called lists in python)
arr = [1,2,3]
print(arr)

# can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

# insert is O(n)
arr.insert(1,7) #since it's an array you can insert at pos, value
print(arr)

# random value access is O(1)
arr[0] = 0
arr[3] = 0
print(arr)

# init arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# -1 is not out of bounds, it's the last value
arr = [1,2,3]
print(arr[-1])

# sublists (aka slicing) first value inclusive, last exclusive
arr = [1,2,3,4]
print(arr[1:3])

# similar to for-loop ranges, last index is non-inclusive
print(arr[0:4])

# unpacking is assigning values from array to variable, but need even amnt
a,b,c = [1,2,3]
print(f'{a} {b} {c}')
print(a, b, c)


# practice with dicts and hashsets
sentence = "This is a sentence."
