import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Generate random 3d data
x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(x, y, z,label="Random 3D data", color="red", marker="o")
