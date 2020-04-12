import numpy as np
'''a = np.array([[1,2],
                [3,4]
                ])
b = np.array([[5,6],
              [7,8]])

print("Array Present\n",a,b)
print(np.vstack((a,b)))
print(np.hstack((a,b)))
c = [9,6]
print(np.row_stack((a,c)))
print(np.concatenate((a,b),1))
## Spliting
arr = np.array([[1,2,3,4,5,6],
                [7,8,9,10,12,14]])
print(np.vsplit(arr,2))
print(np.hsplit(arr,2))
print(np.array_split(arr,2))
today = np.datetime64('2020-02-11')
print(today)
print(np.datetime64(today,'Y'))
dates = np.arange('2017-02','2017-03',dtype ='datetime64[D]')
print(dates)
dur = np.datetime64('2017-05-22') - np.datetime64('2016-05-22')
print(dur)
print(np.timedelta64(dur,'W'))

print(np.sort(np.array(['2017-05-31','2017-05-28','2017-05-21'])))
'''
A = np.array([[6,4,1],
              [4,-2,5],
              [6,3,7]])
print(np.linalg.matrix_rank(A))
print(np.trace(A))
print(np.linalg.det(A))
print(np.linalg.inv(A))
print(np.linalg.matrix_power(A,3))
# Linear Alegebra
# X + 2Y = 10   # 2X + 5Y = 10
# coefficients
a = np.array([[1,2],
             [2,5]])
# Constants
b = np.array([10,10])
print(np.linalg.solve(a,b))