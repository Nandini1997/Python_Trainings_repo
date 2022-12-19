if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score_list=set(arr)
    max_score=max(score_list)
    score_list.remove(max_score)
    print(max(score_list))