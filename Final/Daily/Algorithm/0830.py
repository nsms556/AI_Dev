from collections import deque

GIDUNG, BO = 0, 1

def avail(item, answer) :
    if item[2] == GIDUNG :
        return (item[0], item[1]-1, GIDUNG) in answer or (item[0]-1, item[1], BO) in answer or item[1] == 0
    else :
        return (item[0], item[1]-1, GIDUNG) in answer or (item[0]+1, item[1]-1, GIDUNG) or ((item[0]-1, item[1], BO) in answer and (item[0]+1, item[1], BO) in answer)

def solution(n, build_frame) :
    answer = [[]]

    for x, y, a, b in build_frame :
        if b == 0 :
            pass
        else :
            pass

    return answer