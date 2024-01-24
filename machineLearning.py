# NOTE FOR BRAZILIAN PEOPLE -------> Por favor leia o código com o nome machineLearningBrazil.md
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

# The initial shoot for the first experience
first_shoot = set_shooting_level()

# Creating a function that can get a random action (if something is reached the bot get rewards)
def get_action(current_state,reward):
  avaiable_action = []
  print("avaiable rewards:\n",reward)
  print("Trying level", current_state, "shoot:")
  tries = 1
  for action in enumerate(reward[current_state]):
    print("Try number", tries)
    print("Shoot: ", action)
    if action[1] != -1:
      avaiable_action.append(action[0])
    tries += 1

# Calling the function
get_action(first_shoot, rewards)

# Explanation of the code:
# The objective is making a functional shooting bot;
# The bot tries a random level of shooting, it can be easy or hard;
# Based on how hard the bot get the level, he get more points than in a easier level;
# In all levels if the bot misses, he loses 1 point
# This first push is just for starting setting the reward list, the get_action and set_shooting_level function.