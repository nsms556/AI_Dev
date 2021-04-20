def solution(L, x):
    answer = [idx for idx, data in enumerate(L) if data == x]
        
    if len(answer) == 0 :
        answer.append(-1)
        
    return answer