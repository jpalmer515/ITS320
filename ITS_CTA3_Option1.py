#Program Name: Ferrari Value Calculator
#Author: Jacob Palmer
#Date: 26 Feb 24
#---------------------------------------
#Pseudocode: Create a user input for the year.
# Use an if-else statement to control the flow of information and which output it will trigger.
# Use either a list or range to encompass all ranges of years.
#---------------------------------------
#Program Inputs: Any 4 digit year
#Program Outputs: A numerical value for the year the vehicle was built.

year = input("Enter Vehicle Year:")

if int(year) < 1962:
    print("Too old!")
elif int(year) in range(1962, 1965):
    print("$18,500")
elif int(year) in range(1965, 1969):
    print("$6,000")
elif int(year) in range(1969, 1972):
    print("$12,000")
elif int(year) in range(1972, 1976):
    print("$48,000")
elif int(year) in range(1976, 1981):
    print("$200,000")
elif int(year) in range(1981, 1986):
    print("$650,000")
elif int(year) in range(1986, 2013):
    print("$35,000,000")
elif int(year) in range(2013, 2015):
    print("$52,000,000")
else:
    print("Invaluable")