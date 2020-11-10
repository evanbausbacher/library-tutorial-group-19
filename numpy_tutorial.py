import numpy as np

#all numpy arrays are of type ndarray
#to create an ndarray we can pass any array-like object such as a list or tuple into the array() method to
#be converted into an ndarray

#creating a 0-D array
zeroArr = np.array(9) #0-d array with the value 9
print(zeroArr)
print(type(zeroArr))
print('number of dimensions {}'.format(zeroArr.ndim))
print('-' * 100)

#creating a 1-D array
oneArr = np.array([1,2,3,4,5])
print(oneArr)
print(type(oneArr))
print('number of dimensions {}'.format(oneArr.ndim))
print('-' * 100)

#creating a 2-D array
twoArr = np.array([[1,3,5,7], [2,4,6,8]])
print(twoArr)
print(type(twoArr))
print('number of dimensions {}'.format(twoArr.ndim))
print('-' * 100)

#creating a 3-D array
threeArr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(threeArr)
print(type(threeArr))
print('number of dimensions {}'.format(threeArr.ndim))
print('-' * 100)

