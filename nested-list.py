#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    name_score_list = []
    score_list = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        name_score_list.append([name, score])
        score_list.append(score)

    score_list.remove(min(set(score_list)))
    max_second_score = min(score_list)

    output_list = []
    for i in range(len(name_score_list)):
        if max_second_score == name_score_list[i][1]:
            output_list.append(name_score_list[i][0])

    sorted(output_list)
    for i in sorted(output_list):
        print(i)