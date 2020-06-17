
# Convention for importing matplotlib pyplot module
# Pyplot contains functions for generatng charts and plots
import matplotlib.pyplot as plt 

# List of the first 5 squared numbers and input values
inputs = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Styles for plotting
plt.style.use('seaborn')

# First function returns tuple containing figure and axes objects into variables fig and ax
# We then plot with ax.plot our squares data
fig, ax = plt.subplots()
ax.plot(inputs, squares, linewidth=3)

# Set title and labels
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set tick label size
ax.tick_params(axis='both', labelsize=14)

# Matplotlib viewer and displays plot (adds functionality such as saving and navigation)
plt.show() 

