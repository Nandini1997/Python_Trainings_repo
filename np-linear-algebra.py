#https://www.hackerrank.com/challenges/np-linear-algebra/problem
import numpy
num = int(input())
arr_list = []
for i in range(num):
    arr_list.append(input().split())

input_list = numpy.array(arr_list, dtype=float)
print(round(numpy.linalg.det(input_list), 2))
