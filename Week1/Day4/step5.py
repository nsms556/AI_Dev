import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    
    while True :
        min1 = heapq.heappop(scoville) 
        if min1 > K :
            break
        elif len(scoville) == 0 :
            answer = -1
            break

        newSco = min1 + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, newSco)
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))