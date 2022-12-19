#https://www.hackerrank.com/challenges/python-time-delta/problem
import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    time1=datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    time2=datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    return (str(abs(time1-time2).total_seconds())).split(".")[0]
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)