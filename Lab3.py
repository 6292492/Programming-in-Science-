import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).
def polar_to_cartesian(r, theta):

    x=r*math.cos(math.radians(theta))
    y=r*math.sin(math.radians(theta))
    return (round(x,5), round(y,5))
r=float(input("What is radius in cartesian plane"))
theta=float(input("What is the angle (in degrees) in the polar plane"))
print(f"The coordinate are {polar_to_cartesian(r, theta)} in the cartesian plane")
# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):
    r=math.sqrt(x**2+y**2)
    theta=(math.degrees(math.atan(y/x)))
    return (r, theta)
y=float(input("What is y coordiante in cartesian plane"))
x=float(input("What is x coordinate in cartesian plane"))
print(f"The polar coordinates are {cartesian_to_polar(x, y)} in the polar plane")

# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, f, phi, t):
    x_t=A*math.cos(2*math.pi*f*t+phi)
    phi=math.radians(theta)
    return x_t
f=float(input("What is frequency of oscillation")) # in Hz
phi=float(input("What is initial condition of motion"))
A=float(input("What is the amplitude of the motion"))
t=float(input("What is the time"))
print=(f"The position of the oscillatory motion at any given time is {pendulum_position(A, f, phi, t)}")

