def runner_up(list1):
    list2 = list(set(list1))
    list2.sort()
    return list2[-2]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    score = runner_up(arr)
    print(score)
