import math

def dist(a, b):
    """Compute the distance between two x,y points."""
    x0, y0 = a  # Destructuring assignment
    x1, y1 = b
    
    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

a = (2, 7)   # <-- x,y coordinates stored in tuples
b = (-14, 72)

# Prints "Distance is 66.94"
print("Distance is: {:.2f}".format(dist(a, b)))


# Write a function `print_tuple` that prints all the values in a tuple

# YOUR CODE HERE
def print_tuple(t):
    for i in t:
        print(i)
        

t = (1, 2, 5, 7, 99)
print_tuple(t)  # Prints 1 2 5 7 99, one per line

# Declare a tuple of 1 element then print it
# u = (1)  # What needs to be added to make this work?
# print_tuple(u)
def print_tuples(t):
    print(t)
        

# Declare a tuple of 1 element then print it
u = (1)  # What needs to be added to make this work?
print_tuples(u)