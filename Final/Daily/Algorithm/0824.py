# 0824 외벽점검
# https://programmers.co.kr/learn/courses/30/lessons/60062

def solution(n, weak, dist):  
    W, D = len(weak), len(dist)
    check_list = [()]
    new_weak = weak + [x + n for x in weak]
    #print(new_weak)
    
    new_dist = dist[::-1]
    #print(new_dist)

    cnt = 0
    for d in new_dist :
        checks = []
        cnt += 1

        for i, point in enumerate(new_weak) :
            start = point
            ends = new_weak[i:n+i]
            can = [end % n for end in ends if end - start <= d]
            checks.append(set(can))

        #print(checks)

        cand = set()
        for c in checks :
            for x in check_list :
                new = c | set(x)
                #print(new)
                if len(new) == W :
                    return cnt
                cand.add(tuple(new))
            #print(check_list)
        check_list = cand

    return -1


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

if __name__ == '__main__' :
    print(solution(n, weak, dist))