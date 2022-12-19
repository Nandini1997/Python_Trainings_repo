#https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy
numpy.set_printoptions(legacy='1.13')


my_list = list( map(float,input().split()))
print( numpy.floor(my_list))
print( numpy.ceil(my_list))
print( numpy.rint(my_list))