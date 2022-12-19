#https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
import numpy
dim_1,dim_2=input().split()
arr=[]
arr1=[]
for i in range(int(dim_1)):
    arr.append(list(map(int,input().split())))


print(numpy.mean(numpy.array(arr),axis=1))
print(numpy.var(numpy.array(arr),axis=0))
print(round(numpy.std(numpy.array(arr),axis=None),11))