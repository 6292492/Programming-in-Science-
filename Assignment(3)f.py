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
def density_plot(data, color_map='gray'):  
   plt.hist2d(data[:, 0], data[:, 1], bins=50, cmap=color_map, density=True)
   plt.colorbar(label="Density")
   plt.xlabel("X Axis")
   plt.ylabel("Y Axis")
   plt.title("Density Plot")
   plt.show()

# Example usage:
# Example for plot_curve
x = np.linspace(0, 10, 100)
print(x)
y = np.sin(x)
print(y)
plot_curve(x, y)
    
# Example for plot_hr_diagram
temp = np.array([3000, 5000, 7000, 9000, 11000])
lum = np.array([0.1, 1, 10, 100, 1000])
plot_hr_diagram(temp, lum)

# Example for plot_density
np.random.seed(0) # if your seed is not zero they will all be the same so it will always be same 1000 numbers
data = np.random.randn(100000, 2)  # Generating random 2D data
plot_density(data, 'hot')
