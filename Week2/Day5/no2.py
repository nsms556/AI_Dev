def solution(arr):
    conf = sorted(sorted(arr, key = lambda x : x[0]), key=lambda x : x[1])

    print(conf)

    time = 0
    answer = 0

    for i in range(len(conf)) :
        if conf[i][0] >= time :
            time = conf[i][1]
            answer += 1
            print(time)

    return answer

print(solution([[1, 2], [2, 4], [2, 2]]))
print(solution([[1, 4], [2, 6], [4, 7]]))
print(solution([[3, 4], [2, 6], [1, 3]]))