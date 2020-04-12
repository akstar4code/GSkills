import numpy as np
'''arr_list = np.array(([1,2,3,4],[4,5,4,6],[1,2,0,5]),'i')
print('Array from List')
print(arr_list,arr_list.dtype,type(arr_list),sep = ' ~~~ ')
arr_tup = np.array(((4,5,6,7),(7,8,9,6)),'i')
print('Array from Tuple')
print(arr_tup)
arr_zeros = np.zeros((3,4))
print('Array from Zeros')
print(arr_zeros)
arr_comp = np.full((3,4),6,dtype = complex)
print('Array from Complex Full')
print(arr_comp)
arr_rand = np.random.random((2,2))
print('Array from Random')
print(arr_rand)
arr_arange = np.arange(0,26,5)
print('Array from Arange')
print(arr_arange)
arr_linspace = np.linspace(0,5,10)
print('Array from Linspace')
print(arr_linspace)
print('Original Array : ')
print(arr_list)
newarr = arr_list.reshape(2,2,3)
print('Array Reshape  : ')
print(newarr)
print('Original Array : ')
print(newarr)
print('Array from Flatter: ')
flatt = newarr.flatten()
print(flatt)
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print('Array with first 2 rows and alternatecolumns(0 and 2):')
print(arr[:2,::2])
print('Crossponding elements at coordinates : ')
print(arr[[0,1,2,3],[3,2,0,1]])
print('Elements greater than 4')
print(arr[arr>4])'''
'''new_array = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print(new_array)
print('Multiplied by 10')
print(new_array*10)
new_array *= 10
print('Multiplied by 10')
print(new_array)
print('Transpose of array: ')
print(new_array.T)
print('Largest Elements in Each Coloumn Array : ')
print(new_array.max(axis=1))
print('Sum of all elements : ')
print(new_array.sum()) #for particular axis == 1
print('Commulative sum : ')
print(new_array.cumsum(axis=1))
a = np.array([[1,2],
     [3,4]])
b = np.array([[7,8],
              [2,5]])
print(a+b)
print(a.dot(b))
new_a = np.array([0,np.pi/2,np.pi])
print(np.sin(new_a))
'''
dtypes = [('name','S10'),('grade',int),('cgpa',float)]
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
arr = np.array(values,dtypes)
print('Sorting of array : ')
print(np.sort(arr,order='name'))
print(np.sort(arr,order=['grade','cgpa']))