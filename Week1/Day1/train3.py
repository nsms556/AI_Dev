def solution(L, x):
    answer = -1
    
    front = 0
    end = len(L) - 1
    
    while front <= end :
        middle = int((front + end) // 2)
        if L[middle] == x :
            answer = middle
            break
        elif L[middle] < x :
            front = middle + 1
        else :
            end = middle - 1
    
    return answer

'''
0 1 2 3 4 5  6  7  8   9
0 2 4 6 8 10 15 40 100 1000

90
f e m
0 9 4
5 9 7
8 9 8
8 7 break
return -1

6
f e m
0 9 4
0 3 1
2 3 2
3 3 3
return 3

5
f e m
0 9 4
0 3 1
2 3 2
3 3 3
3 2 break
return -1

'''