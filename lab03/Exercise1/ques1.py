# I. a Python program to square and cube every number in a given list of integers using Lambda. 

num=[1,2,3,4,5,6,7,8,9,10]
square=list(map(lambda x: x ** 2, num))
cube=list(map(lambda x : x ** 3, num))

print("Original list:", num)
print("Squared list:", square)
print("Cubed list:", cube)

