# II. a Python program to find if a given string starts with a given character using Lambda. 

starts_with = lambda s, c: s[0] == c  

text = input("Enter a string: ")  
char = input("Enter the 1st char: ")  

if starts_with(text, char):  
    print("Yes")  
else:  
    print("No")  
