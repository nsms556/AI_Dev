def solution(v):
    answer = []

    x = []
    y = []

    for item in v :
        x.append(item[0])
        y.append(item[1])

    for item in set(x) :
        if x.count(item) == 1 :
            answer.append(item)

    for item in set(y) :
        if y.count(item) == 1 :
            answer.append(item)

    return answer

v = [[1, 4], [3, 4], [3, 10]]
print(solution(v))