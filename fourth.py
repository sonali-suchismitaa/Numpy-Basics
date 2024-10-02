import numpy as np

a = np.arange(0,18).reshape((6,3))
b = np.arange(20,38).reshape((3,6))

'''print(a+b)  #same as np.add(a,b)
print(np.subtract(b,a))  #same as print(b-a)
print(np.multiply(a,b))
print(np.divide(a,b))
print(a@b)  #array multiplication, ***make sure that it follows mXn * nXm
#same as a.dot(b)'''

'''print(b.max())  #max 
print(b.argmax())  #index of max
print(a.min())  #min
print(a.argmin())   #index of min'''

'''print(np.sum(b, axis = 1))  #prints sum of all rows, there are 3 rows in this case
print(np.sum(b, axis = 0)) #prints sum of all cols, there are 5 cols in this case


print(np.sqrt(a))
print(np.std(a)) #standard deviation of the array
print(np.log(b))'''