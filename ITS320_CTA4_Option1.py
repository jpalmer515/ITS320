#Name: Five Floating Number Points
#Author: Jacob Palmer
#Date: 9 MAR 24
#---------------------------------------------------------------------------------------------------------------------
#Pseudocode: Declare a list for the numbers and a list for the numbers after interest is calculated
# Declase variables for each value being asked for
# Add a length check so that the input request will stop after 5
# Use a while loop to fill the list with the requested number of inputs
# Use a for loop to iterate through the numbers in the list, having them run through the calculations for each computation
# Add in checks for number size when asking for user input, replacing the minimal number and adding to the interest list
#---------------------------------------------------------------------------------------------------------------------
#Program Inputs: 5 numbers, great than -100, but less than a really large number
#Program Outptus: Total of all numbers, average of all numbers, largest number, smallest number, and a 20% interest of
# each number in the list.
#----------------------------------------------------------------------------------------------------------------------

numberlist = []
interest = []
maxLength = 5
total = 0
average = 0
max = float(-100)
min = float(99999999999)
interest_value = 0

while len(numberlist) < maxLength:
    number = float(input("Enter a number: "))
    if number >= -100:
        numberlist.append(number)
    else:
        print("Too low, choose a higher number")
    for i in numberlist:
        total = sum(numberlist)
        average = total/len(numberlist)
    if number >= -100:
        interest_value = (number + number*0.2)
        interest.append(interest_value)
    else:
        pass
    if number < min and number >= -100:
        min = number
    else:
        pass
    if number > max:
        max = number
    else:
        pass
print('\nTotal =',total)
print('Average =',average)
print('Maximum =',max)
print('Minimum =',min)
print('Interest =',interest,'\n')