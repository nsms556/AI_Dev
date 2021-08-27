# 08.24 외벽점검
# https://programmers.co.kr/learn/courses/30/lessons/60062


def solution(n, weak, dist) :
    cnt = 0
    dist.reverse()

    for d in dist :
        cnt += 1
    
    
    new_dist = set()
    for w in weak :
        for wa in weak :
            tmp = abs(wa - w)
            new_dist.add(tmp)
            print(tmp, end=' ')
        print()
    #print(new_dist)


n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]

#n = 12	
#weak = [1, 3, 4, 9, 10]
#dist = [3, 5, 7]

solution(n, weak, dist)
