import numpy as np

list_data = [1,2,3]
array = np.array(list_data)

print(array.size) # 몇 개의 데이터로 이루어져 있는지
print(array.dtype) # numpy 데이터가 어떠한 자료형을 가지고 있는지
print(array[2])