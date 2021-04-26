def attackable(locations, candLoc) :
    nowRow = len(locations)
    for row in range(nowRow) :
        if locations[row] == candLoc or abs(locations[row] - candLoc) == abs(nowRow - row) :
            return False
    
    return True

def find_loc(locations, row, n, result) :
    if row == n :
        result.append(locations[:])
        return
    
    for candLine in range(n) :
        if attackable(locations, candLine) :
            locations.append(candLine)
            find_loc(locations, row+1, n, result)
            locations.pop()

def solution(n):
    result = []
    find_loc([], 0, n, result)

    answer = len(result)
    
    return answer

'''
[2, 0, 3, 1]
[1, 3, 0, 2]

i + j
    0   1   2   3
0   0   1   2   3
1   1   2   3   4
2   2   3   4   5
3   3   4   5   6

i - j
    0   1   2   3
0   0  -1  -2  -3
1   1   0  -1  -2
2   2   1   0  -1
3   3   2   1   0



'''