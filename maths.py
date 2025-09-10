import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return np.power(x,2) + x - 10
x = np.linspace(-10, 10, 100)
# x axis values
x = [1, 2, 10]
# corresponding y axis values
y = [1, 2, 10]

# plotting the points
plt.plot(x, f(x), color='blue')

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Baba Graphen')

# function to show the plot
plt.show()
