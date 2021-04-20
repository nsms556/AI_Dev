def solution(L, x):
    idx = None
    
    for i in range(len(L)) :
        if x < L[i] :
            idx = i
            break
            
    if idx == None :
        idx = len(L)
        
    L.insert(idx, x)
    return L