#https://www.hackerrank.com/challenges/iterables-and-iterators/problem
from itertools import combinations

number=int(input())
string=input().split(" ")
slice_index=int(input())
output_list=[]
combination_str= list(combinations(string,slice_index))
for i in combination_str:
    if 'a' in i:
        output_list.append(list(i))
print(round(len(output_list)/len(combination_str),12))