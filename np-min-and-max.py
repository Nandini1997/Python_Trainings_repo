#https://www.hackerrank.com/challenges/np-min-and-max/problem
import numpy

dim_1, dim_2 = input().split()
my_list = []
for i in range(int(dim_1)):
    my_list.append(list(map(int, input().split())))

max_num = numpy.min(numpy.array(my_list), axis=1)
print(numpy.max(max_num))