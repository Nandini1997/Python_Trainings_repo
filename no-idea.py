#https://www.hackerrank.com/challenges/no-idea/problem
m, n = input().split()
arr_list = list(map(int, input().split()))
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

happiness=0

for i in arr_list:
    if i in A_list:
        happiness=happiness+1
    if i in B_list:
        happiness=happiness-1
print(happiness)