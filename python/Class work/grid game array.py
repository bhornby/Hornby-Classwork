#initiation grid for game and assigning randm location of treasure
import random

grid =[[0 for row in range(10)] for col in range(10)]

treasure_row = random.randint(0,10)
treasure_col = random.randint(0,10)

#the treasure is located at the location where grid[row][col] == 1
grid[treasure_row][treasure_col] = 1
