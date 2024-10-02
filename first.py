import numpy as np

'''a = np.array([1,2,3,4,5])
print(a)

b = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])
print((b))

c = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(c)

d = np.array([[1,2,3],
              [4,5,6],
              [7,8,9],
              [10,11,12]])
print(d)
print(type(a))
print(type(b))
print(type(c))

print(a.size)
print(b.size)
print(c.size)
print(d.size)

print(a.shape)   #gives row, col
print(b.shape)
print(c.shape)
print(d.shape)

print(a.dtype) #prints datatype

print(c.transpose()) '''

'''print(np.empty((4,4), dtype = float))

x = np.ones(6)
print(x)

print("\n")

y = np.ones((3,5))
print(y)

print("\n")

z = np.ones((3,5), dtype = int)
print(z)'''

# we can do the same for zeroes by writing np.zeroes((row, col), dtype)

'''a = np.ones((4,8), dtype = str)
print(a)
print("\n")
b = np.zeros((4,8), dtype = str)
print(b)'''

a = np.ones((4,8), dtype = bool)  #ones for true
b = np.zeros((4,8), dtype = bool) #zeros for false
print(a) 
print("\n")
print(b)