import numpy as np

#################################################################################################
# 1. Create arrays using NumPy                                                                  #
#  All numpy arrays are of type ndarray. To create an ndarray we can pass any array-like object #
#  such as a list or tuple into the array() method to be converted into an ndarray.             #
#################################################################################################

# Create a 0-D array
zeroArr = np.array(9) # 0-d array with the value 9
print(zeroArr)
print(type(zeroArr))
print('number of dimensions {}'.format(zeroArr.ndim))
print('-' * 100)

# Create a 1-D array
oneArr = np.array([1,2,3,4,5])
print(oneArr)
print('number of dimensions {}'.format(oneArr.ndim))
print('-' * 100)

# Create a 2-D array
twoArr = np.array([['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']])
print(twoArr)
print('number of dimensions {}'.format(twoArr.ndim))
print('-' * 100)

# Create a 3-D array
threeArr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(threeArr)
print('number of dimensions {}'.format(threeArr.ndim))
print('-' * 100)

# Create a higher dimensional array
multiArr = np.array(['n = 6'],ndmin=6)
print(multiArr)
print('number of dimensions {}'.format(multiArr.ndim))
print('-' * 100)

#################################################################################################
# 2. Index and Slice arrays using NumPy                                                         #
#  Indexes in numpy arrays are zero-indexed, so they start with 0. You can access an array      #
#  element by providing its index number. Slicing takes elements from a starting index, up to   #
#  but not including, an ending index. You can also pass a step value to change the count size  #
#  of indexes within the range. If no start index is passed it is assumed to be 0. If no end    #
#  index is passed it is assumed to be the length of the array, so it includes the remainder of #
#  the elements. If no step is passed then it is assumed to be 1                                #
#################################################################################################

# Index a 1-D array
#  Prints the second element in the array 
print(oneArr[1])
print('-' * 100)

# Slice a 1-D array 
#  Prints the third and fourth element since the end index is excluded 
print(oneArr[2:4])
print('-' * 100)

# Index a 2-D array
#  Prints the letter g by accessing the ['e', 'f', 'g', 'h'] list which is the second element in
#  the first dimension then selects 'g' which is the 3rd element in the second dimension  
print(twoArr[1,2]) 
print('-' * 100)

# Slice a 2-D array
#  Prints b and c
print(twoArr[0,1:3])
print('-' * 100)

# Slice without specifying start index
#  Prints elements from 0th index up to but not including 3rd index
print(oneArr[:3])
print('-' * 100)

# Slice without specifying end index 
#  Prints elements from the 1st index onward
print(oneArr[1:])
print('-' * 100)

# Negative Slicing
#  Prints the 3rd from last index up to but not icluding index 1 from the end
print(oneArr[-3:-1])
print('-' * 100)

#################################################################################################
# 3. Shaping and Reshaping arrays using NumPy                                                   #
#  The shape of the array is the number of elements in each dimension. The attribute shape is   #
#  a tuple with each index representing the number of elements in that dimension. Reshaping     #
#  allows us to change the dimensionality of our arrays we can reshape to any shape as long as  #
#  the number of elements required is equal in both shapes.                                     #
#################################################################################################

# Shape of the arrays created 
print('shape of 1-D array: {}'.format(oneArr.shape))
print('shape of 2-D array: {}'.format(twoArr.shape))

# Reshaping a 1d array to a 2d array
arr = np.array([1,2,3,4,5,6,7,8])
reshapedArr = arr.reshape(4,2)
print(reshapedArr)
print('-' * 100)

#################################################################################################
# 4. Iterating arrays using NumPy                                                               #
#  Iterating ndarray's are very similar to iterating regular lists in Python. In addition to    #
#  this typical use case, there is also a function called nditer() which helps iterate n        #
#  dimensional arrays without for-loops, so you save a lot of code.                             #
#################################################################################################

# Iterate a 1-D array using the basic for-loop in python
for elem in oneArr:
    print(elem)
print('-' * 100)

# Iterate a 2-D array where lists are printed instead of the individual 2-D elements
for elem in twoArr:
    print(elem)
print('-' * 100)

# Iterate a 2-D array where each individual 2-D element is printed
for row in twoArr:
    for col in row:
        print(col)
print('-' * 100)

# Iterate using the numpy nditer() which helps iterate n dimensional arrays without for-loops
for elem in np.nditer(threeArr):
    print(elem)
print('-' * 100)

#################################################################################################
# 5. Joining and Spliting arrays using NumPy                                                    #
#  Join multiple arrays into one single array using the concatenate() method. You can specify   #
#  the axis that we want to join on (this is 0 if not specified). Split an array into several   #
#  sub arrays using the array_split() method second parameter is the number of arrays you want  #
#  to split into. If the source array has less elements than required, array_split() will       #
#  adjust accordingly whereas the normal split() method will not adjust the elements.           #
#################################################################################################

# Join two arrays and put them into one array using the concatenate() method
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
xy = np.concatenate((x,y))
print(xy)
print('-' * 100)

# Split array into seperate arrays by giving number of arrays to split into with array_split()
#  Returns array of new arrays
arr = np.array([1,2,3,4,5,6,7,8,9,10])
newArrays = np.array_split(arr, 5)
print(newArrays)
print(newArrays[0]) # First array in the list of arrays
print('-' * 100)

#################################################################################################
# 6. Searching and Sorting arrays using NumPy                                                   #
#  Search for a specific value within an array using the where() method. The Result is a tuple  #
#  which contains the indexes where the specified element is in the array. Returns all of the   #
#  indices if the element is in the array more than once. Sort an array using the sort() method #
#  which returns the sorted array.                                                              #
#################################################################################################

# Find the index of a particular element
x = np.where(oneArr == 3)
print(x)
print('-' * 100)

# Find indices for even elements
x = np.where(oneArr%2 == 0)
print(x)
print('-' * 100)

# Find indices for odd elements
x = np.where(oneArr%2 == 1)
print(x)
print('-' * 100)

# Using the searchsorted() method to find the index of where to place an element to maintain
#  sort in the array assumes the array to be used on is sorted.
arr = np.array([1,3,5,7,8,10,15])
x = np.searchsorted(arr, 9)
print(x)
print('-' * 100)

# Sort an array using the sort() method
arr = np.array([1,2,9,67,3,105,10,12])
sortedArr = np.sort(arr)
print(sortedArr)
print('-' * 100)