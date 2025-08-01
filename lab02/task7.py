
#Create a loop that counts from 0 to 100

i=0
while (i<=100):
    print(i)
    i+=1


# Make a multiplication table using a loop

table = int(input("Enter the number whose table you want to print: "))
# note : for k syntax me brackets nhi lgaane hoty!
for i in range(1,11):
    print(table,'*',i,'=',table*i)


#3. Output the numbers 1 to 10 backwards using a loop

a=10
while(a>=1):
    print(a)
    a-=1
    
    
    #. Create a loop that counts all even numbers to 10

e=0
while(e<=10):
    print(e)
    e+=2
    
    
sum=0
for i in range(100,201):
        sum+=i
        print(sum)
    