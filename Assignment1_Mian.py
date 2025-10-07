# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(a,b,c):# function to find max number
    max_num=max([a,b,c])
    return max_num # results in finding max value between the variables
a=float(input("What is value of a:"))#ask user value of a
b=float(input("What is the value of b:"))#ask user value of b
c=float(input("What is value of c:"))#ask user value of c
print(f"the max number is;{built_in_functions_max(a,b,c)}")#this print function determines what number is the max
    
    

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(x,y,z):#function to find minimum between variables
    min_num=min([x,y,z])
    return min_num # results in finding the minumim between variables
x=float(input("What is value of x:"))#ask user for x value
y=float(input("What is the value of y:"))#ask user for y value
z=float(input("What is value of z:"))#ask user fo z value
print(f" the minimum number is;{built_in_functions_min(x,y,z)}")# this print function recallas to function and finds the samllest value

    

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):# function used to complete operation
    if number>0:# conditional statement to be met
        return("It is a posiitve number!")#result if the if statement is met
    elif number<0:# also a conditional statement
        return("It is a negative number!")#result if first condition not met
    else:# conditional statement
        return("It is zero!")#final applicable condition if first two  not met
number=int(input("Enter your number:"))#asks user to input the number 
print(check_number(number))# checks the status of the integer and prints if it is positve, negative,or zero      
    

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    for i in range(1, rows+1):#shows a range of number from 1 to the number of rows
        print("*"*i)# prints the number of stars in each row
rows=int(input("Enter number of rows:"))# ask user for number of rows
star_shape(rows)# recalls the function

    

  

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    count=1
    while count<= limit: # keeps counting the numbers up to the limit given
        if count%3==0:# this equations makes it certain to only consider the multiple of threes
            print("Multiple of 3")
        else:# this takes into consideration all non multiples of three
            print(count)
        count+=1
limit=int(input("Enter the limit:"))# ask user for the limit
count_multiples_of_3(limit)# recalls the function
  

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    sum_even=0
    for i in range(start, end+1):
        if i%2==0:# this makes it to where it only considers the sum of even numbers
            sum_even+=i# takes the sum of all ven numbers in the range
        else:
            continue
    return sum_even # returns to find the sum of all even number from start to end limit placed
start=int(input("Enter a start number:"))# ask user for start number
end=int(input("Enter an end number:"))#ask user fo the end number
print(f"the sum of all even numbers is {sum_of_even_numbers(start, end)}")# prints and finds the sum of all the even numbers
   
