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
def slice_every_nth(lst, val,n):#
    res = []  # List to store the result
    for i in range(len(lst)):
        res.append(lst[i])           # Add the current element
        if (i + 1) % n == 0:         # After every Nth element
            res.append(val)          # Insert the desired value
    return res

# Example usage
a = [1, 2, 3, 4, 5, 6, 7]
result = insert_after_every_n(a, 'X', 2)
print(result)  # Output: [1, 2, 'X', 3, 4, 'X', 5, 6, 'X', 7]


# Function : Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    return 0

# Function : Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):

    return [[0, 0], [0, 0]]
