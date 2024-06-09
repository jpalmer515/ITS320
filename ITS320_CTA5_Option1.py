#Name: String Values in Reverse Order
#Author: Jacob Palmer
#Date: 12 MAR 24
#---------------------------------------------------------------------------------------------------------------------
#Pseudocode: Create a function for the user input
# Use a message to prompt the user. Use a while loop with a false variable to iterate through the input.
# Use a for loop with a range limiter to stop the inputs after 3.
# Append the inputs to the list to concatenate them.
# Use the object.reverse() function to reverse the list.
# Print the list.
#---------------------------------------------------------------------------------------------------------------------
#Program Inputs: Any 3 strings
#Program Outptus: A list of the 3 strings in reverse order.
#----------------------------------------------------------------------------------------------------------------------

def get_inputs():
    words = []
   
    for i in range(0,3):
        input_string = input("enter a string: ")
        words.append(input_string)
   
    for w in reversed(words):
        print(w)

input_words = get_inputs()

# Below is another function that works

def get_inputs_reverse():
    words = []

    for i in range(0,3):
        input_string = input("enter a string: ")
        words.append(input_string)
    words.reverse()

    return words

output_words = get_inputs_reverse()

print(output_words)
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#Below is the fix to my above code. In the name of modularity, I decided to make an input function instead of just making a user
#input and for loop outside of the reverse function. 

def user_requested_inputs():
    list1 = []

    for i in range(0,3):
        user_input = input("Enter a string: ")
        list1.append(user_input)
    
    return list1

def reverse_words(list1):
    new_list = list1[::-1]

    return new_list

final_list = reverse_words(list1=user_requested_inputs())

print(final_list)