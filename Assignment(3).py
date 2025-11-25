import csv  
import matplotlib.pyplot as plt  
import numpy as np 
import math  
# Function 1: File I/O - Writing and Reading from a Text File
# Writes a list of numbers to a file and then reads them back as a list of integers.
def write_and_read_txt(filename, numbers):  
    with open(filename, "w") as f:  # open file for writing
        for n in numbers:  # loop numbers
            f.write(str(n) + "\n")  # write each number

    result = []  # list for reading
    with open(filename, "r") as f:  # open file for reading
        for line in f:  # loop lines
            result.append(int(line.strip()))  # convert back to int
    return result  # return list
print("FUNCTION 1 OUTPUT:")
print(write_and_read_txt("numbers.txt", [1, 2, 3, 4, 5]))
print()
# Function 2: File I/O - Writing and Reading from a CSV File
# Writes a list of lists to a CSV file and reads it back.
def write_and_read_csv(filename, data):  
    with open(filename, "w", newline="") as f:  # open CSV
        writer = csv.writer(f)  # writer object
        writer.writerows(data)  # write all rows

    result = []  # list for reading
    with open(filename, "r") as f:  # open CSV
        reader = csv.reader(f)  # reader object
        for row in reader:  # loop rows
            result.append(row)  # append row list
    return result  # return list of lists
print("FUNCTION 2 OUTPUT:")
print(write_and_read_csv("data.csv", [[1, 2], [3, 4], [5, 6]]))
print()
# Function 3: Reading an Array from a File
# Reads a space-separated array from a text file and converts it to a NumPy array.
def read_array_from_file(filename):  
    with open(filename, "r") as f:  # open file
        data = f.read()  # read entire file
    nums = data.split()  # split by spaces
    nums = [float(x) for x in nums]  # convert to floats
    return np.array(nums)  # return numpy array
with open("array.txt", "w") as f:  # create file
    f.write("1 2 3 4 5")  # space-separated numbers
print("FUNCTION 3 OUTPUT:")
print(read_array_from_file("array.txt"))
print()
# Function 4: Plotting Data with plot() and show()
# This function plots a given list of numbers as a line graph.
def plot_data(numbers):  
    plt.plot(numbers)  # simple line plot
    plt.title("Line Plot")  # title
    plt.xlabel("Index")  # x label
    plt.ylabel("Value")  # y label
    plt.show()  # display plot
print("FUNCTION 4 OUTPUT: Showing line plot...")
plot_data([1, 3, 2, 5, 4])  # example
print()
# Function 5: Density Plot
# This function takes a list of numbers and plots a density plot.
def density_plot(data):  
    mean = np.mean(data)  # mean
    std = np.std(data)  # standard deviation

    x_vals = np.linspace(mean - 4*std, mean + 4*std, 100)  # x range
    y_vals = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_vals - mean) / std) ** 2)  # density formula

    plt.plot(x_vals, y_vals)  # plot curve
    plt.title("Density Plot")  # title
    plt.xlabel("Values")  # label
    plt.ylabel("Density")  # label
    plt.show()  # show plot


# PRINT TEST for Function 5
print("FUNCTION 5 OUTPUT: Showing density plot...")
density_plot([12, 15, 14, 16, 15, 14, 17, 13, 15])
