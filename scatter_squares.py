## A note on this module.
## The data here is meaningless, but the customization tips are good practice

# Scatter plot for least-squares

import matplotlib.pyplot as plt

# List of the first 5 squared numbers and input values
inputs = range(1,1001)
squares = [x**2 for x in inputs]

plt.style.use('seaborn')
# Adding a number indicates number of subplots generated
# Refer to each subplot by index [n], starting from 0
fig, ax= plt.subplots(2)

# Create points for scatter plot, with customizations such as size, color, etc.
ax[0].scatter(inputs, squares, c='red', s=10)

# This generates a colormap where cmap is the colormapping
# Basically darker equates to a higher value
ax[1].scatter(inputs, squares, c=squares, cmap=plt.cm.Blues, s=10)

# Set title and labels
ax[0].set_title('Square Numbers', fontsize=24)
ax[0].set_xlabel("Value", fontsize=14)
ax[0].set_ylabel("Square of Value", fontsize=14)

# Set tick label size
ax[0].tick_params(axis='both', which = 'major', labelsize=14)

# Set the range for each axis.
ax[0].axis([0, 1100, 0, 1100000])

plt.show()

# Can replace plt.show() with this next line to auto save the plot
# plt.savefig('squares_plot.png', bbox_inches='tight')