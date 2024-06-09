#Name: Cars Dictionary
#Author: Jacob Palmer
#Date: 24 FEB 24
#---------------------------------------------------------------------------------------------------------------------
#Pseudocode: Create a prompt allowing a user to add multiple variables, using the .split function so separate them.
# Create a standard dictionary with keys for each value listed in the assignment.
# Found that it would b easier to have a list in each key so that values can be added to the list.
#---------------------------------------------------------------------------------------------------------------------
#Program Inputs: Brand, model, year, starting odometer, ending odometer, estimated mpg.
#Program Outptus: The entire dictionary with the lists showing the user input data as the last item in each list.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
cars = {'brand': ['Alpina', 'BMW'], 'model': ['B7', 'M3'], 'year': ['2021', '2025'], 'start_odo': ['500', '15'], 'end_odo': ['600', '99'], 'est_mpg': ['10', '36']}

a, b, c, d, e, f = input("Enter vehicle brand, model, year, starting odometer, ending odometer and estimated mpg:").split(",")

if 'brand' in cars:
    cars['brand'].append(a)

if 'model' in cars:
    cars['model'].append(b)

if 'year' in cars:
    cars['year'].append(c)

if 'start_odo' in cars:
    cars['start_odo'].append(d)

if 'end_odo' in cars:
    cars['end_odo'].append(e)

if 'est_mpg' in cars:
    cars['est_mpg'].append(f)

print(cars)