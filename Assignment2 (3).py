# Function : Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(a):
    res = list(set(a))# Remove duplicates by converting to a set
    res.sort() # Sort the list
    return res
numbers = [1, 3, 4, 5, 2, 3, 5, 6, 7, 9, 8, 7]# list of numbers to arrange using function
print(remove_duplicates_and_sort(numbers))# calls back to function and arrnages the numbers in orderd list
# Function : Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []  # List to store cumulative sums
    total = 0    # Running total

    for num in arr:
        total += num       # Add the current number to the running total
        result.append(total)  # adds the sum to the list that is returned by function

    return result
numbers = [1, 2, 3, 4, 5] # numbers listed to work with to find the sum of them
print(cumulative_sum(numbers))  # calls back to function and prints out what is needed

   

# Function : Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    result=[]
    for i in range(0,len(lst),step): # skips step
        result.append(lst[i]) # implements every Nth value
    return result
lst=[1,2,3,4,5,6,7]
print(slice_every_nth(lst))

    

    
    



# Function : Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
   result=0  #initially making the dot product start at zero
   for i in range(len(list1)):
        result += list1[i]*list2[i]
   return result
list1=[1,2,3,4]
list2=[5,6,7,8]
print(f"dot product of {list1} and {list2} is {dot_product(list1, list2)}")

# Function : Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):

    return [[0, 0], [0, 0]]
