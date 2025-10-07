# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(a,b,c):# function to find max number
    return(max(a,b,c))# results in finding max value between the variables
a=int(input("What is value of a:"))#ask user value of a
b=int(input("What is the value of b:"))#ask user value of b
c=int(input("What is value of c:"))#ask user value of c
built_in_functions_max(a,b,c)#allows for the inside of fucntion to be recalled
    
    

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(x,y,z):#function to find minimum between variables
    return(min(x,y,z))# results in fidning the minumim between variables
x=int(input("What is value of x:"))#ask user for x value
y=int(input("What is the value of y:"))#ask user for y value
z=int(input("What is value of z:"))#ask user fo z value
built_in_functions_min(x,y,z)# allows to recall to the function

    

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):# function used to complete operation
    if num>0:# conditional statement to be met
        return("It is a posiitve number!")#result if the if statement is met
    elif num<0:# also a conditional statement
        return("It is a negative number")#result if first condition not met
    else:# conditional statement
        return("It is zero")#final applicable condition if first two  not met
num=int(input("What is the integer?"))#asks user to input the number 
check_number(number)# allows the terminal to call back to function       
    

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    

  

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    # TODO: Implement this function
    pass  # Replace with your code

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    # TODO: Implement this function
    pass  # Replace with your code
