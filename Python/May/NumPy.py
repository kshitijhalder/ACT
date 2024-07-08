"""
NumPy - Numerical Python
        - immutable array
            - faster than list
                - more memory efficient than list
        
Date : 24.04.2024
Date : 25.04.2024                   [UPDATED]
Date : 1.05.2024                    [UPDATED]
Date : 8.05.2024                    [UPDATED]
"""
import os
import numpy as np      #type: ignore

os.system('clear') 
# Syntax: numpy.array(object, shape, dtype=None, copy=True, order='K', subok=False, ndmin=0)
# Create a 1D array
arr1 = np.array([1, 2, 3])
print("Array 1: \n",arr1)
print("Array 1: ",arr1[0])
print("Array type: ",type(arr1))

# Create a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nArray 2: \n",arr2)

# Create a 3D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\nArray 3: \n",arr3)

#Empty array
arr4 = np.empty((2,3))
print("\nEmpty Array: \n",arr4)

# Array of zeros
arr5 = np.zeros((2,3))
print("\nArray of zeros: \n",arr5)

# Array of ones
arr6 = np.ones((2,3), dtype=int)
print("\nArray of ones: \n",arr6)

# Check the number of dimensions
print("\nNumber of dimensions in Array 1: ",arr1.ndim)
print("Number of dimensions in Array 2: ",arr2.ndim)
print("Number of dimensions in Array 3: ",arr3.ndim)
print("Number of dimensions in Empty Array: ",arr4.ndim)

# Difference between zeros and empty
print("\nDifference between zeros and empty: ")

# Convert Celsius to Fahrenheit
list1 = [33.5, 37.5, 39.5]
#list2[0] = 34.5         #array is immutable
list2 = np.array(list1)
#print(list1 * 9/5 + 32)
print(list2 * 9/5 + 32)

# Addition  of Array
arr7 = arr2 + arr2
print("\nAddition of Array 2: \n",arr7)

# Subtraction of Array
arr8 = arr2 - arr1
print("\nSubtraction of Array 2: \n",arr8)

# Multiplication of Array
arr9 = arr2 * arr1
print("\nMultiplication of Array 2: \n",arr9)

# Identity Matrix
arr10 = np.eye(3, dtype=int)
print("\nIdentity Matrix: \n",arr10)

# Random number array
arr11 = np.random.uniform(-10**9, 10, (2, 3))
#arr11 = np.random.randint(-10**9, 10, (2, 3))
print("\nRandom number array: \n",arr11)

"""
Normalised array -
            mean - mean is the average of the numbers
            std - standard deviation is the square root of the variance
            variance - variance is the average of the squared differences from the mean
            z-score - z-score is the number of standard deviations from the mean
            normalisation - normalisation is the process of scaling the data to have a mean of 0 and a standard deviation of 1
            normalised data - normalised data is the data that has been scaled to have a mean of 0 and a standard deviation of 1
            normalised array - normalised array is the array that has been scaled to have a mean of 0 and a standard deviation of 1
            normalised matrix - normalised matrix is the matrix that has been scaled to have a mean of 0 and a standard deviation of 1
"""
arr12 = np.random.normal(0, 0.1, (2, 4))
print("\nNormalised array: \n",arr12)

# Mean, Standard Deviation, Shape, Size, Itemsize, Ndim #

print(arr12.mean())
print(arr12.std())
# Shape shows the number of rows and columns
print(arr2.shape)
# Size shows the number of elements in the array
print(arr12.size)
# Itemsize shows the size of each element in the array
print(arr12.itemsize)
# Ndim shows the number of dimensions in the array
print(arr12.ndim)

# Diagonal multiplication of array [for diagonal elements]
print("Before arr2: \n",arr2)

"""
for i in range(arr2.shape[1]):
    arr2[i, i] *= 2
print(arr2)
"""
"""
for i in range(len(arr2)):
      arr2[i][i] *= 2
"""

# Date edited - 25.04.2024
# Diagonal multiplication of array [for non diagonal elements]
for i in range(len(arr2)):
      arr2[i, i] *= 2
      for j in range(len(arr2)):
            if i != j:
                  arr2[i, j] *= 2
print("After arr2: \n",arr2)
print(len(arr2))

# Reshape the array
arr13 = arr2.reshape(1, 9)
print("\nReshape the array: \n",arr13)

# Concatenate the array
# Syntax: numpy.concatenate((a1, a2, ...), axis=0, out=None)
# axis is the axis along which the arrays will be joined
arr14 = np.concatenate((arr2, arr2), axis=1)
print("\nConcatenate the array: \n",arr14)

# Array slicing
# Syntax: numpy.arange(start, stop, step, dtype=None)
print("\nArray slicing: ")
arr15 = np.arange(0, 11, 2)
print(arr15.reshape(2, 3))

# Flags
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nArray 2 Flags :")
print(arr2.flags)
#arr2.setflags(write=False)
#arr2.flags.writeable = False                   #TypeError: assignment destination is read-only
arr2[0,0] = 100      # [0,0] is an element   
#arr2[0] = 100       # [0] is a row   
print(arr2)

# Copy
arr16 = arr2.copy()
arr16[0,0] = 1
print("\nBefore Copy:")
print(arr2)
print("After Copy:")
print(arr16)

# View
arr17 = arr2.view()
arr17[0,0] = 2200
print("\nBefore View:")
print(arr2)
print("After View:")
print(arr17)

# Split
# Syntax: numpy.split(ary, indices_or_sections, axis=0)
arr18 = np.array([1, 2, 3, 4, 5, 6])
print("\nSplit array:")
print(np.split(arr18, 6))
print(np.split(arr18, [2, 4]))

# Where     
# Syntax: numpy.where(condition[, x, y])
arr19 = np.array([[1, 2, 3], [3, 5, 6], [7, 8, 9]])
print("\nWhere:")
arr20 = np.where(arr19 == 3)
print(arr20)
print("Type of arr20:",type(arr20))

# Change the value of the array
for i in range(len(arr20)):
      arr19[arr20[0][i], arr20[1][i]] = 10
print(arr19)

"""
# Print a graph of the array
import matplotlib.pyplot as plt                 #type: ignore  
arr21 = np.array([(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16)])
#plt.plot(arr3)
#plt.show()

import matplotlib.pyplot as plt                 #type: ignore
from mpl_toolkits.mplot3d import Axes3D         #type: ignore

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the cube
vertices_large = np.array([(0, 0, 0),
                           (1, 0, 0),
                           (1, 1, 0),
                           (0, 1, 0),
                           (0, 0, 1),
                           (1, 0, 1),
                           (1, 1, 1),
                           (0, 1, 1)])

# Define the vertices of the smaller cube
vertices_small = vertices_large / 2       # scale down by a factor of 2

# Translate the smaller cube to the center of the larger cube
vertices_small += 0.25                    # translate by half the side length of the larger cube

# Define the edges of the cube
edges = [(0, 1), (1, 2), (2, 3), (3, 0),  # bottom edges
         (4, 5), (5, 6), (6, 7), (7, 4),  # top edges
         (0, 4), (1, 5), (2, 6), (3, 7)]  # side edges

# Plot the edges of the larger cube
for edge in edges:
    v1, v2 = edge
    ax.plot(*zip(vertices_large[v1], vertices_large[v2]), color = 'b')

# Plot the edges of the smaller cube
for edge in edges:
    v1, v2 = edge
    ax.plot(*zip(vertices_small[v1], vertices_small[v2]), color = 'b')

# Connect the corresponding vertices of the larger and smaller cubes
for v_large, v_small in zip(vertices_large, vertices_small):
    ax.plot(*zip(v_large, v_small), color='b')  # plot in red

plt.show()

# Assuming arr21 is a 2D array with three columns
arr21 = np.array([(0,0,0),(2,0,0),(0,2,0),(2,2,0),(0,0,2),(2,0,2),(0,2,2),(2,2,2),
                  (1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1),(2,1,0),
                  (1,2,0),(1,0,2),(0,1,2),(2,1,2),(1,2,2),(2,2,1),(1,2,1),(2,1,1),
                  (1,1,2),(0,2,1),(2,0,1)])

# Extract each column from arr21
x = arr21[:, 0]
y = arr21[:, 1]
z = arr21[:, 2]

#ax.scatter(x, y, z)
#ax.plot(x, y, z)

for i in range(1, len(arr21)):
    if arr21[i, 1] == arr21[i-1, 1]:
        ax.plot(arr21[i-1:i+1, 0], arr21[i-1:i+1, 1], arr21[i-1:i+1, 2])

plt.show()
"""

# Date edited - 1.05.2024
# Check if the matrix is square
print("\nCheck if the matrix is square:\n")
shape = arr2.shape

if shape[0] == shape[1]:
    print("The matrix is square")
else:
     print("The matrix is not square")

"""
Logspace -
   Syntax - numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)
    start - the starting value of the sequence
    stop - the end value of the sequence
    num - the number of samples to generate
    endpoint - if True, stop is the last sample, otherwise, it is not included
    base - the base of the logarithm
    dtype - the data type of the output array
    axis - the axis along which the sequence is generated

"""
arr21 = np.logspace(start= 1, stop= 10, num= 10, base= 10)
print("\nLogspace: \n",arr21)

# Date edited - 8.05.2024
# Ndarray
# Syntax: numpy.ndarray(shape, dtype=float, buffer=None, offset=0, strides=None, order=None)
arr22 = np.ndarray((2, 3), dtype=float)
print("\nNdarray: \n",arr22)

# Function stacks
# Syntax: numpy.stack(arrays, axis=0, out=None, shape=None)
                            # axis - the axis is used to stack the arrays vertically or horizontally
arr23 = np.stack((arr1, arr1), dtype=float)
print("\nStacks: \n",arr23)
print("Reshhape: \n",arr23.reshape(3, 2))

# Ones_alike
# Syntax: numpy.ones_like(a, dtype=None, order='K', subok=True, shape=None)
arr24 = np.ones_like(arr23, shape=(3, 2))
print("\nOne alike: \n",arr24)