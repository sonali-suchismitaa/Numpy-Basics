import numpy as np

a = np.arange(1,51)
a = a.reshape(10,5)
print(a)

'''print(a[0])  #0th row
print(a[1,3])  #1st row, 3rd column
print(a[2:5])  #print from 2nd row to 4th row
print(a[0:10])'''

'''print(a[:, 2])  #all rows 2nd col shall be printed

print(a[2:5,2])  #from 2nd row to 4th row (5th is excluded), 2nd col shall be printed'''

print(a[:, 2:5])  #all rows, 2nd to 5th col shall be printed

print(a[:,:].dtype)