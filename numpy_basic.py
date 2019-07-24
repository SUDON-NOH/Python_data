import numpy as np
import time

# Terminal 에서 pip package 설치하기

# pip install '모듈명'
# pip uninstall '모듈명'

# PyCharm 안에서 package 설치하기

# File -> settings -> project interpreter

data1 = [0, 1, 2, 3, 4, 5]
print(type(data1))              # <class 'list'>
print(data1)                    # [0, 1, 2, 3, 4, 5]

a1 = np.array(data1)                                            # array - method
print(type(a1))                 # <class 'numpy.ndarray'>       # numpy - module ndarray - class
print(a1)                       # [0 1 2 3 4 5]                 # a1 - instance 객체

print(a1.dtype)                 # a1.dtype 은 instance member

a2 = np.arange(6)
print(type(a2))                 # <class 'numpy.ndarray'>
print(a2)                       # [0 1 2 3 4 5]
print(a2.shape)                 # (6, ) 1차원


a3 = np.arange(12).reshape(3, 4)
print(type(a3))                 # <class 'numpy.ndarray'>
print(a3)
                                # [[ 0  1  2  3]
                                #  [ 4  5  6  7]
                                #  [ 8  9 10 11]]
print(a3.shape)                 # (3, 4) 2차원
print(a3.ndim)                  # 2


a4 = np.arange(12).reshape(3, 2, 2)
print(a4)
                                # [[[ 0  1]
                                #   [ 2  3]]
                                #  [[ 4  5]
                                #   [ 6  7]]
                                #  [[ 8  9]
                                #   [10 11]]]
print(a4.shape)                 # (3, 2, 2)
print(a4.ndim)                  # 3

# Indexing & Slicing

print(a4[0, 0, 0], a4[0, 0, 1])
print(a4[0, 1, 0], a4[0, 1, 1])
print(a4[1, 0, 0], a4[1, 0, 1])
print(a4[1, 1, 0], a4[1, 1, 1])
print(a4[2, 0, 0], a4[2, 0, 1])
print(a4[2, 1, 0], a4[2, 1, 1])

print('-'*50)

for x in range(3):
    for y in range(2):
        for z in range(2):
            # print(a4[x, y, z])
            print(a4[x][y][z], end = ',')
print()

print(a4[0])
                    # [[0 1]    2차원 - Slicing
                    #  [2 3]]
print(a4[0][0])
                    # [0 1]     1차원 - Slicing
print(a4[0][0][0])
                    # 0          - Indexing
print(a4[0, 0, 0])
                    # 0          - Indexing

# 조건 인덱싱

a5 = np.arange(12).reshape(2, 2, 3)
print(a5)
print(a5.shape)

print(a5[a5>5])     # [ 6  7  8  9 10 11]
print(a5[a5<3])     # [0 1 2]

# 시간측정
start_time = time.time()
for x in range(2):
    for y in range(2):
        for z in range(3):
            # print(a5[x][y][z], end =',')
            if a5[x][y][z] > 5 :
                print(a5[x][y][z])
end_time = time.time()
elapsed_time = end_time - start_time
print('Start time:', start_time,'\n''End time:', end_time,'\n''Elapsed time:',elapsed_time,'\n')
print()

# 슬라이싱
print(a5[:,:,:2])
print(a5[:-1,:-1,:-1])


d = np.arange(12).reshape(3, 4)

print(d[::-1])       # 행의 순서가 반대로 변화
                                       # [[ 8  9 10 11]
                                       #  [ 4  5  6  7]
                                       #  [ 0  1  2  3]]
print(d[:,::-1])     # 열의 순서가 반대로 변화
                                       # [[ 3  2  1  0]
                                       #  [ 7  6  5  4]
                                       #  [11 10  9  8]]
print(d[::-1, ::-1]) # 행과 열의 순서를 모두 반대로 변경
                                       # [[11 10  9  8]
                                       #  [ 7  6  5  4]
                                       #  [ 3  2  1  0]]