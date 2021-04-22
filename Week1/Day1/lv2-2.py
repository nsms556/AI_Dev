from itertools import combinations

def solution(m, weights):
    combi = []
    
    for i in range(len(weights)) :
        combi.extend(list(combinations(weights, i)))
    
    count = 0
    for item in combi :
        if sum(item) == m :
            count += 1

    return count

m = 3000
w = [500, 1500, 2500, 1000, 2000]

print(solution(m, w))
