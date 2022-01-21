import numpy as np
list1 = list(map(int, input().split()))
arr = np.array(list1)
print (np.reshape(arr,(3,3)))
