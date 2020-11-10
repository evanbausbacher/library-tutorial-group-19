# NumPy Tutorial

## Installation:

To install with `pip`, you can use the following command in your terminal: 

```pip install numpy```

To install with `conda`, you can use the following command in you terminal:

```conda install numpy```

## Setup:

To setup your NumPy environment, you can use the following Python code at the top of your script:

```import numpy```


## Use NumPy:

1. Create arrays using NumPy

```
# Create a 0-D array
zeroArr = np.array(9) # 0-d array with the value 9
print(zeroArr)
print(type(zeroArr))
print('number of dimensions {}'.format(zeroArr.ndim))
```
```
# Create a 1-D array
oneArr = np.array([1,2,3,4,5])
print(oneArr)
print('number of dimensions {}'.format(oneArr.ndim))
```
```
# Create a 2-D array
twoArr = np.array([['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']])
print(twoArr)
print('number of dimensions {}'.format(twoArr.ndim))
```
```
# Create a 3-D array
threeArr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(threeArr)
print('number of dimensions {}'.format(threeArr.ndim))
```
```
# Create a higher dimensional array
multiArr = np.array(['n = 6'],ndmin=6)
print(multiArr)
print('number of dimensions {}'.format(multiArr.ndim))
```
2. Index and Slice arrays using NumPy

```
# Index a 1-D array
print(oneArr[1]) # prints the second element in the array 

# Slice a 1-D array 
print(oneArr[2:4]) # prints the third and fourth element since the end index is excluded 
```
```
# Index a 2-D array
print(twoArr[1,2]) 
```
```
# Slice a 2-D array
print(twoArr[0,1:3])
```
```
# Slice without specifying start index
print(oneArr[:3])
```
```
# Slice without specifying end index 
print(oneArr[1:])
```
```
# Negative Slicing
print(oneArr[-3:-1])
```
3. Shaping and Reshaping arrays using NumPy

```
# Shape of the arrays created 
print('shape of 1-D array: {}'.format(oneArr.shape))
print('shape of 2-D array: {}'.format(twoArr.shape))
```
```
# Reshaping a 1d array to a 2d array
arr = np.array([1,2,3,4,5,6,7,8])
reshapedArr = arr.reshape(4,2)
print(reshapedArr)
```
4. Iterating arrays using NumPy

```
# Iterate a 1-D array using the basic for-loop in python
for elem in oneArr:
    print(elem)
```
```
# Iterate a 2-D array where lists are printed instead of the individual 2-D elements
for elem in twoArr:
    print(elem)
```
```
# Iterate a 2-D array where each individual 2-D element is printed
for row in twoArr:
    for col in row:
        print(col)
```
```
# Iterate using the numpy nditer() which helps iterate n dimensional arrays without for-loops
for elem in np.nditer(threeArr):
    print(elem)
```
5. Joining and Spliting arrays using NumPy

```

```
6. Searching and Sorting arrays using NumPy

```
# Find the index of a particular element
x = np.where(oneArr == 3)
print(x)
```
```
# Find indices for even elements
x = np.where(oneArr%2 == 0)
print(x)
```
```
# Find indices for odd elements
x = np.where(oneArr%2 == 1)
print(x)
```
```
# Using the searchsorted() method to find the index of where to place an element to maintain
#  sort in the array assumes the array to be used on is sorted.
arr = np.array([1,3,5,7,8,10,15])
x = np.searchsorted(arr, 9)
print(x)
```
```
# Sort an array using the sort() method
arr = np.array([1,2,9,67,3,105,10,12])
sortedArr = np.sort(arr)
print(sortedArr)
```
