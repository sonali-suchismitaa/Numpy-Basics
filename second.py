import numpy as np

'''a = np.arange(1,20)
print(a) 

b = np.arange(1,20,2)  #print odd numbers
print(b)

c = np.arange(2,20,2)  #print even numbers
print(c)

print("\n")

c = c.reshape((3,3))
print(c)'''

a = np.arange(1,100,2)
a = a.reshape((10,5)) #reshape converts 1D to mXn dimensions
print(a)

a = a.flatten()  #flatten onverts mXn to 1D 
print(a)

a = a.ravel()
print(a)


'''
diff b/w ravel and flatten:
a.flatten() : 1. Return copy of original array.
              2. If you modify any value of this array, value of original is not affected.
              3. flatten() is comparatively slower than ravel() as it occupies memory.
              4. flatten is a method of an ndarray object
a.ravel() :   1. Return only reference/ view of original array.
              2. If you modify the array you would notice that the value of original array also changes.
              3. ravel() is faster than flatten().
              4. ravel is a library-level function.
'''