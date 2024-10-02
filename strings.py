import numpy as np

s1 = "My name is Sonali"
s2 = "I want to live in Edinburgh"

'''int(np.char.add(s1,s2)) #merges the strings
print(np.char.upper(s1))
print(np.char.lower(s2))'''

print(np.char.split(s1))

s3 = "My name is \nSonali"
print(np.char.splitlines(s3))

print(np.char.replace(s1, "Sonali", "Shnehal"))

print(np.char.center('Sonali is a good girl', 30, '*'))