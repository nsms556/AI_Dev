def solution(L, x, l, u) :
    if l > u :
        return -1
    mid = (l + u) // 2

    if x == L[mid] :
        return mid
    elif x < L[mid] :
        return solution(L, x, l, mid-1)
    else :
        return solution(L, x, mid+1, u)

l = [2, 5, 7, 9, 11]

print(solution(l, 4, 0, 4))

''' 
빈칸 채우기 

L2  : l > u
L8  : solution(L, x, l, mid-1)
L10 : solution(L, x, mid+1, u)

'''
