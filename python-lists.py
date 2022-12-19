#https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(N):
        input_string = input().split()

        if 'insert' in input_string:
            my_list.insert(int(input_string[1]), int(input_string[2]))
        if 'print' in input_string:
            print(my_list)
        if 'remove' in input_string:
            my_list.remove(int(input_string[1]))
        if 'append' in input_string:
            my_list.append(int(input_string[1]))
        if 'sort' in input_string:
            my_list.sort()
        if 'pop' in input_string:
            my_list.pop()
        if 'reverse' in input_string:
            my_list.reverse()