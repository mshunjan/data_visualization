import matplotlib.pyplot as plt 

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True: 
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk() 

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()

    # Generates list of points and then a color map of the walk based on those points
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.show()

    # Takes in user input to generate a new walk
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break