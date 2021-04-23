def solution(n, lost, reserve):
    answer = 0
    
    uniform = [1] * (n+2)

    for i in lost :
        uniform[i] -= 1

    for i in reserve :
        uniform[i] += 1

    rsv = [x for x in reserve if x not in lost]

    for i in sorted(rsv) :
        if uniform[i-1] == 0 :
            uniform[i-1] = 1
            uniform[i] = 1
        elif uniform[i+1] == 0 :
            uniform[i+1] = 1
            uniform[i] = 1
    
    return n - uniform.count(0)

print(solution(10, [1,3,5,7,8], [2,5,6,7,9]))