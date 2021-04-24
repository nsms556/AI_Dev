import heapq

def solution(n, works):
    answer = 0

    works = [-x for x in works]
    heapq.heapify(works)

    for i in range(n) :
        tmp = heapq.heappop(works)
        if tmp >= 0 :
            heapq.heappush(works, tmp)
            break

        tmp += 1
        heapq.heappush(works, tmp)

    if len(works) > 0 :
        for w in works :
            answer += w ** 2

    return answer

print(solution(4, [4,3,3]))
print(solution(1, [2,1,2]))
print(solution(3, [1,1]))
print(solution(20, [1,2,4,3,4,65,9,8,7,15,15,4,70,75,2]))
#print(solution(1000000, [x for x in range(2000)]))
