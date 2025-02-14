# NumPy is a library module which gives us more possible ways
# to calculate or generally make use of numbers in 1D, 2D, 3D, etc.
import numpy as np
# we cant work with numpy without importing here of course

something = np.array([2,5,1,6,4,7])
something = something * 2
print(something)
# Here we easily multiply the whole list by 2 with numpy

ss1 = np.array([1, 2, 3])
ss2 = np.array([4, 5, 6])
ss3 = np.array([3, 7, 5])
result = ss1 + ss2 + ss3
print(result)
# Here we are making use of 2D way of numpy by adding columns to columns


# Overall numpy is way better at perfoming numerical operations than Python and has much less memory usage.
# So NumPy is just ideal library for numerical operations