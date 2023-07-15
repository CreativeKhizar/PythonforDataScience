# Create NumPy arrays from Python Data Structures, Intrinsic NumPy objects and Random Functions.

import numpy as np
a1=np.array((1,2,3))
print(a1)
a2=np.indices((3,3))
print(a2)
a=np.array([7,6,5])
b=np.zeros((4,3))
print(b)
c=np.arange(20)
d=np.random.rand(2,3)
e=np.linspace(5,7,4)
print(d)
print(c)
print(a)
print(e)


f=np.ones((8,9))
print(f)
g=np.random.randn(2,3)
print(g)
h=np.eye(3,3)
print(h)
i=np.random.randint(1,3,size=(3,3))
print(i)
