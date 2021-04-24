''' 좌석 구매 '''

def solution(seat):
    sold = set(tuple(s) for s in seat)

    answer = len(sold)

    return answer

print(solution([[1,1],[2,2],[3,3]]))
print(solution([[1,1],[2,1],[1,2],[3,4],[2,1],[2,1]]))
