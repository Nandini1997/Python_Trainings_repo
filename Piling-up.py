#https://www.hackerrank.com/challenges/piling-up/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
no_testcases=int(input())
for i in range(no_testcases):
    num=int(input())
    my_list=list(map(int,input().split()))
    deque_list=deque(my_list)
    right_ele=deque_list.pop()
    left_ele=deque_list.popleft()
    if left_ele>right_ele:
        current_ele=left_ele
    else:
        current_ele=right_ele
    flag=False
    while(len(deque_list)>0):
        if(left_ele>=right_ele and left_ele <=current_ele):
            current_ele=left_ele
            left_ele=deque_list.popleft()
            latest=left_ele
        elif(right_ele>=left_ele and right_ele<=current_ele):
            current_ele=right_ele
            right_ele=deque_list.pop()
            latest=right_ele
        else:
            flag=True
            break
    if flag or latest>current_ele:
        print("No")
    else:
        print("Yes")