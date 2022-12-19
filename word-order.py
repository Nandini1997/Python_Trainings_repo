#https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
count=int(input())
arr=[]

for i in range(count):
    arr.append(input())

print(len(set(arr)))

my_dict=Counter(arr)

for i in my_dict.values():
    print(i,end=" ")