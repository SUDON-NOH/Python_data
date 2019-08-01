import numpy as np

# 3 * X0 + 2 * X1 - 4 * X2 = 52
# 2 * X0 - 4 * X1 + 9 * X2 = -27
# 5 * X0 + 3 * X1 - 7 * X2 = 86




A = np.mat("3, 2, -4; 2, -4, 9; 5, 3, -7")
b = np.array([52, -27, 86])

print(A)
print(b)
x = np.linalg.solve(A, b)
print(x)
print(np.dot(A, x))

#=====================================================================================================
# 교수님 답
# # numpy활용실습문제.py
#
# import numpy as np
#
# # 1번
# # 3*X0 + 2*X1 - 4*X2 = 52
# # 2*X0 - 4*X1 + 9*X2 = -27
# # 5*X0 + 3*X1 - 7*X2 = 86
# # X0 = 10
# # X1 = 5
# # X2 = -3
# A = np.mat("3 2 -4;2 -4 9;5 3 -7")
# print("A\n", A)
# b = np.array([52, -27, 86])
# print("b\n", b)
#
# x = np.linalg.solve(A, b)
# print("Solution : ", x)  # [10.  5. -3.]
# print('Check:', np.dot(A, x))
#
# # 역행렬로 답 구하기
# inverse = np.linalg.inv(A)
# x = np.dot(inverse, b)
# print('using inverse:', x)
#
#
# # 2번
#
# def mydot(a, b):
#     r = np.arange(a.shape[0] * b.shape[1]).reshape(a.shape[0],
#                                                    b.shape[1])
#     for i in range(a.shape[0]):
#         for j in range(b.shape[1]):
#             c = a[i, :] * b[:, j]
#             r[i][j] = c.sum()
#     return r
#
#
# # (m,n) * (n,l) = (m,l)
# a = np.arange(6).reshape(2, 3)
# b = np.arange(6).reshape(3, 2)
# print('\na.dot(b):')
# print(a.dot(b))
# print('\nmydot(a,b):')
# print(mydot(a, b))
# # [[10 13]
# #  [28 40]]
#
# a = np.arange(24).reshape(4, 6)
# b = np.arange(54).reshape(6, 9)
# print('\na.dot(b):')
# print(a.dot(b))
# print('\nmydot(a,b):')
# print(mydot(a, b))
# # a.dot(b):
# # [[ 495  510  525  540  555  570  585  600  615]
# #  [1305 1356 1407 1458 1509 1560 1611 1662 1713]
# #  [2115 2202 2289 2376 2463 2550 2637 2724 2811]
# #  [2925 3048 3171 3294 3417 3540 3663 3786 3909]]
# #
# # mydot(a,b):
# # [[ 495  510  525  540  555  570  585  600  615]
# #  [1305 1356 1407 1458 1509 1560 1611 1662 1713]
# #  [2115 2202 2289 2376 2463 2550 2637 2724 2811]
# #  [2925 3048 3171 3294 3417 3540 3663 3786 3909]]