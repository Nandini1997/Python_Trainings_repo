#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
student_number=int(input())
student_column=input().split()
students_details = namedtuple('Student', student_column)

sum=0
for i in range(student_number):
    student = students_details._make(input().split())
    sum=sum+float(student.MARKS)

average=sum/student_number
print("%.2f" %average)