# Decides which move to make each time a step is taken
from random import choice 

class RandomWalk:
    ''' A class to generate random walks. ''' 

    def __init__(self, num_points=5000):
        ''' Initialize attributes of a walk. '''
        # Points in the walk
        self.num_points = num_points

        # All walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        ''' Calculates the points in the walk. '''
        # Keep taking steps until walk reaches desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go (right or left) 
            x_direction = choice([1,-1])
            # Chooses how far to go in that direction by selecting a random  number on the chosen range
            x_distance = choice(range(0,6))
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            # Continue makes it so we ignore these.

            if x_step and y_step ==0:
                continue 

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

