def solution(d, budget):
    answer = 0
    
    dSort = sorted(d)
    
    for item in dSort :
        if budget - item >= 0 :
            answer += 1
            budget -= item
    
    return answer