def solution(number, k):
    q = []
    for idx, num in enumerate(number) :
        while len(q) > 0 and q[-1] < num and k > 0 :
            q.pop()
            k -= 1
        
        if k == 0 :
            q.extend(list(number[idx:]))
            break
        
        q.append(num)
        
    if k > 0 :
        q = q[:-k]
        
    return ''.join(q)