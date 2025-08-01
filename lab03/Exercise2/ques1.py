#  You have collected information about cities in your province. You decide to store each city’s
#  name, population, and mayor in a file. Write a python program to accept the data for a number 
#  of cities from the keyboard and store the data in a file in the order in which they’re entered


f= open('CitiesDetails.txt', 'a')
f.write('file me data daaldo \n')


while True:
    x = int(input("Press 1 to enter city details, and 2 to close file :  "))
    if(x == 2):
        f.close()
        break
    city_name = input("Enter city name : ")
    city_population = input("Enter population of city : ")
    city_mayor = input("Enter City Mayor : ")
    line = f"{city_name}, {city_population}, {city_mayor} \n" #\n for line change 
    f.write(line)