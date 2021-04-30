
def solution(n,signs):
    queue = []

    for start in range(n) :
        for dst in [idx for idx, x in enumerate(signs[start]) if x == 1] :
            queue.insert(0, [start, dst])
    
    while queue :
        start, dst = queue.pop()
        
        new_dsts = [idx for idx, x in enumerate(signs[dst]) if x == 1]

        for new_dst in new_dsts :
            if signs[start][new_dst] == 0:
                signs[start][new_dst] = 1
                queue.insert(0, [start, new_dst])

    return signs

print(solution(3, [[0,1,0],[0,0,1],[1,0,0]]))
print(solution(3, [[0,0,1],[0,0,1],[0,1,0]]))

'''

0 1 0       0 0 1
0 0 1       0 0 1
1 0 0       0 1 0

0 1 1       0 1 1
1 0 1       0 1 1
1 1 0       0 1 1

1 1 1       
1 1 1
1 1 1





'''