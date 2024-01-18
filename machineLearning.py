# Importing libraries
import numpy as np 
import random

# Creating reward list
rewards = [
    [-1,1,1,1,1,1], # Bigger place to shoot = less points
    [-1,-1,10,10,10,10],
    [-1,-1,-1,100,100,100],
    [-1,-1,-1,-1,1000,1000],
    [-1,-1,-1,-1,-1,10000] # Smaller place to shoot = plus points
]

# This function randomizes the shooting level
def set_shooting_level():
    return np.random.randint(0,5)

# Printing an example of the shooting level:
print("Example: randomized shooting level as", set_shooting_level())


