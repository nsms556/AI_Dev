def solution(n):
    block = [0, 1, 2]

    for i in range(3, n+1) :
        block.append((block[i-1] + block[i-2]) % 1000000007)

    answer = block[n]

    return answer

print(solution(50002))