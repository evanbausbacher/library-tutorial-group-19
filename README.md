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

3. Shaping and Reshaping arrays using NumPy


4. Iterating arrays using NumPy


5. Joining and Spliting arrays using NumPy


6. Searching and Sorting arrays using NumPy

