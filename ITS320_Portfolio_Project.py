#Name: Portfolio Project
#Author: Jacob Palmer
#Date: 6 APR 24
#---------------------------------------------------------------------------------------------------------------------
#Pseudocode: Create a dealer class with a constructor and private variables
# Use private variables as user inputs
# Start with a main class with a constructor, adding vehicles and printing the inventory
# - calling the main function with "add_car1", outside of main class works, but calling it for 2 causes them to combine
# into a single list. Each vehicle instance needs to be its own list. Use a list of lists.
# - Use the list index to reference each vehicle for updates and removals
# - defining variables in main constructor causes them to needed for program to run, remove them
# Use a try/except method to capture ValueError when requesting integers for model year and mileage
# Find inventory menu options to add a menu
# - defining if/else statements under the add_new_vehicle method restricted modularity and the code could be moved
# outside to be their own functions
# - Updating/removing don't need to be their own functions
# Create an inventory class that will handle an inventory variable, printing the inventory and exporting the inventory
# Inventory list nested in the inventory class
# Reference Codecademy for examples on calling a method in a class from another class (Python 3 - Classes)
# Call the main method to retrieve vehicle information
# - after calling the main method, output is only printing the object memory location... 
# - create a string using the vehicle inputs, that will be called by the view_inventory function
# - indices are populating correctly, but need to redefine where the print statement breaks
# Menu options are letters, use .upper() to avoid errors with lower-case letters
# Use if/else logic to iterate through each list letter option, (A, U, R, V, E)
# When calling an empty list, no return. Add return information if the list is empty
# Indices were off by 1, title screen index=0
# Create a function for exporting the list to local file, using 'W' so that files are always up to date. 
# - Using 'a' would append each list to the text file, making a single large file each iteration the export is called
#---------------------------------------------------------------------------------------------------------------------
#Program Inputs: Select menu option A, U, R, V, E. Then input vehicle information accordingly.
#Program Outptus: Will output strings to confirm your action is complete. Outputs a list of lists, showing vehicle information
# and vehicle index in the inventory. Will export list to a local folder in the form of a text file. New files will overwrite
# the preview, rename the text file if you want to save multiple.
#----------------------------------------------------------------------------------------------------------------------

class dealer_automobiles:
    #Constructor
    def __init__(self):
        self._v_make = ''
        self._v_model = ''
        self._v_color = ''
        self._v_year = 0
        self._v_mileage = 0

    def add_new_vehicle(self):
        try:
            self._v_make = str(input('Enter vehicle make: '))
            self._v_model = str(input('Enter vehicle model: '))
            self._v_color = str(input('Enter vehicle color: '))
            self._v_year = int(input('Enter a 4 digit vehicle model year: '))
            self._v_mileage = int(input('Enter vehicle mileage: '))
            return True
        except ValueError:
            print('Please try entering vehicle information again using only whole numbers for the mileage and year built.')
            return False
    #Function for returning a input vehicle information in a string format, allowing the string to be stored in a human readable format            
    def __str__(self):
        return ' '.join(str(m) for m in [self._v_make.upper(), self._v_model.upper(), self._v_color.upper(), self._v_year, self._v_mileage])

class dealer_inventory():
    #Constructor
    def __init__(self):
        self.vehicles = []
        
    def add_vehicle(self):
        new_vehicle = dealer_automobiles()
        if new_vehicle.add_new_vehicle() == True:
            self.vehicles.append(new_vehicle)
            print('\n Vehicle has been added \n')
            
    def view_inventory(self):
        print('\n')
        print(' '.join([' ', 'MAKE', 'MODEL', 'COLOR', 'YEAR', 'MILEAGE']))
        for index, vehicle in enumerate(self.vehicles):
            #Shows the index number of the vehicle, starting at 1
            print(f'{index+1}', end=' ')
            print(vehicle)
        print('\n')
            
    def output_text_file(self):
        #Designating filepath for text file to be created
        with open ('INSERT FILEPATH HERE', 'w') as inventory_file:
            #Adding a header and line-break to the top of the text file
            inventory_file.write('   MAKE MAKE MODEL COLOR MILEAGEe')
            inventory_file.write('\n')
            #Adding all vehicles to the text file
            for vehicle in inventory.vehicles:
                inventory_file.write(f'\n {vehicle}')
            print('File exported')
            
#Variable for dealer_inventory() class
inventory = dealer_inventory()

while True:
    
    #Front facing menu for users to choose their option
    print('Hello, welcome to Assorted Autos!')
    print('Please choose an option below.')
    print('---------------------------------')
    print('A) Add a new vehicle')
    print('U) Update an existing vehicle')
    print('R) Remove an existing vehicle')
    print('D) Display vehicle inventory')
    print('E) Export vehicle inventory')
    #Input given with a .upper() function to account for any lowercase letters   
    user_input = input('Select an Option: ')
    choice = user_input.upper()
    
    if choice == 'A':
        inventory.add_vehicle()
    elif choice == 'U':
        #Checking if there's anything in the inventory
        if len(inventory.vehicles) <= 0:
            print('\n Inventory is empty \n')
        car_index = int(input('Enter the index number of the vehicle to be updated: '))
        #Checking that the car_index doesn't go lower than the lowest index in the list
        if car_index-1 > len(inventory.vehicles):
            print('\n Invalid index number')
        else:
            dealer = dealer_automobiles()
            if dealer.add_new_vehicle() == True:
                inventory.vehicles[car_index-1] = dealer      #does this indexing work properly?
                print('\n Vehicle has been updated \n')
    elif choice == 'R':
        if len(inventory.vehicles) <= 0:
            print('\n Inventory is empty \n')
        car_index = int(input('Enter the index number of the vehicle to be removed: '))
        if car_index-1 > len(inventory.vehicles):
            print('Invalid index number \n')
        else:
            #Using car_index-1 to account for the list headers being in the first index
            inventory.vehicles.remove(inventory.vehicles[car_index-1])
            print('\n Vehicle removed \n')
    elif choice == 'D':
        if len(inventory.vehicles) <= 0:
            print('\n Inventory is empty \n')
        else:
            #Calling the view_inventory function
            inventory.view_inventory()
    elif choice == 'E':
        if len(inventory.vehicles) <= 0:
            print('\n Inventory is empty \n')
        else:
            #Calling the output_text_file function
            inventory.output_text_file()