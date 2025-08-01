

# LAB #01 task:

# Exercise: Dir and Help 
# Learn about the methods Python provides for strings. To see what methods Python provides for a 
# datatype, use the dir and help commands: 
# >>> s = 'abc'

# 1 Try out some of the string functions listed in dir (ignore those with underscores '_' around the method 
# name). 



s='abc'
print(dir(s))

help(s.find)
help(s.replace)

s='abc'
print(s.capitalize())
print(s.count('b'))
print(s.endswith('c'))
print(s.find('b'))  #finds index of first occurence
print(s.find('e'))
print(s.lower())
print(s.isalpha())
print(s.upper())
print(s.replace('b','f'))

sentence="Artificial Intelligence"
print(sentence.split())  #split string into list

whitespace_str=" abc "
print(whitespace_str.strip())


# Exercise Python input /output Basic operations
# (i)Write a Python program to swap 4 variables values (input four values.
# Sample input:
# Before swapping
# a=2,b=56,c=78,d=9
# After Swapping
# a=,9,b=78,c=56,d=2
# (ii) Write a Python program to convert temperatures to and from celsius,
# Fahrenheit.
# Formula : c/5 = f-32/9
# Expected Output :
# Enter temp in Celsius: 60°C
# Temperature in Fahrenheit is :140

# i:
var1 = int(input("Enter value for var1: "))
var2 = int(input("Enter value for var2: "))
var3 = int(input("Enter value for var3: "))
var4 = int(input("Enter value for var4: "))

print(f"Before swapping: var1={var1},var2={var2},var3={var3},var4={var4}")

var1,var2,var3,var4=var4,var3,var2,var1

print(f"After swapping: var1={var1},var2={var2},var3={var3},var4={var4}")


# ii:
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in fahrenheit is: {fahrenheit}")


# Exercise: Lists 
# (i)Play with some of the list functions. You can find the methods you can call on an object via the dir
# and get information about them via the help command: 
# >>> dir(list) 
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__ge__', 
# '__getattribute__', 
# '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', 
# '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', 
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
# '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__str__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 
# 'remove', 'reverse', 'sort'] 
# >>> help(list.reverse) 
# Help on built-in function reverse: 
# reverse(...) 
#  L.reverse() -- reverse *IN PLACE* 
# >>> lst = ['a','b','c'] 
# >>> lst.reverse() 
# >>> ['c','b','a'] 
# Note: Ignore functions with underscores "_" around the names; these are private helper methods. Press 
# 'q' to back out of a help screen
# (ii)Write a Python program to count the number of strings where the string length is 2 or more and the 
# first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2.


Samplelist = ['abc', 'xyz', 'aba', '1221']
count = 0

for string in Samplelist:
    if len(string) >= 2 and string[0] == string[-1]: 
        count += 1 

print(f"Expected result: {count}") 

# Exercise: Dictionaries 
# (i)Use dir and help to learn about the functions you can call on dictionaries and implement it. 
# (ii)Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# i:
print("Available methods for dictionaries:")
print(dir(dict))

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['b'])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_dict.update({'d' : 4})
print(f"After update: {my_dict}")

# ii:

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result={}
result.update(dic1)
result.update(dic2)
result.update(dic3)

print(f"Result after update: {result}")

concatedres={**dic1,**dic2,**dic3}
print(f"res after concatenation: {concatedres}")

# Exercise: List Comprehensions 
# (i)Write a list comprehension which, from a list, generates a lowercased version of each string that has 
# length greater than five. 
# (ii)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',’Teapink’]
# Expected Output : ['Green', 'White', 'Black']

# i:
strings = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']
result = [s.lower() for s in strings if len(s) > 5]
print("Lowercased strings with length > 5:", result)


# ii:
sample_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']
res = []  
for index, item in enumerate(sample_list):  
    if index not in (0, 4, 5):  
        res.append(item) 
        print("List after removing 0th, 4th, and 5th elements:", res)
        
# Exercise : Operators:
# Play with some Operators in Python(assignment ,bitwise ,logical, arithmetic, identity, membership)
# (i) What will be the output of the given program        

# Identity Operators in Python
x = 6
if (type(x) is int): 
 print ("true") 
else: 
 print ("false")

x = 7.2

if type(x) == float:
    if type(x) is not int:
        print("true")
    else:
        print("false")

 
#  output:True

# Membership operator:

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]

for item in list1:
    if item in list2:
        print("overlapping")
        break
else:
    print("not overlapping")
    
#  Output:not overlapping

# Floor division and Exponent and Assign
a=9
a//=3
a**=5
print("floor divide=", a)
print("exponent=", a)

# Bitwise Operaotors:
# a = 60 /* 60 = 0011 1100 */ 
# b = 13 /* 13 = 0000 1101 */
# int c = 0 
#  c = a & b /* 12 = 0000 1100 */ 
#  print("Line 1", c )
#  c = a | b /* 61 = 0011 1101 */
#  print("Line 2 ", c )
#  c = a ^ b /* 49 = 0011 0001 */
#  print("Line 3 ", c )
#  c = ~a /*-61 = 1100 0011 */
#  print("Line 4", c )
#  c = a << 2 /* 240 = 1111 0000 */
#  printf("Line 5 ", c );
#  c = a >> 2 /* 15 = 0000 1111 */
#  printf("Line 6 -", c );

# output:
#  12
#  61
#  49
#  -61
#  240
#  15