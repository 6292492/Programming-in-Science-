# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    g=9.8
    result=float(h0-1/2*g*t**2)
    return result

h0=float(input("enter height of ball"))
t=float(input("enter the time"))
print(f"the height of the ball after {t} is {calculate_height(h0,t)} meters")

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and 50return the distance traveled by the car.
def calculate_car_distance(t):
    result=distance=speed*time
    return result
speed=20 # meters per second
time=float(input("enter your time"))
print(f"the distance the car traveled after {t} is {calculate_car_distance(t)}")



  