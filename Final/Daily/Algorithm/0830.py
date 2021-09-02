GIDUNG, BO = 0, 1

def unavail(answer) :
    for item in answer :
        x, y, a = item
        if a == GIDUNG :
            if y != 0 and (x, y-1, GIDUNG) not in answer and (x-1,y,BO) not in answer and (x,y,BO) not in answer :
                return True
        else :
            if (x,y-1,GIDUNG) not in answer and (x+1, y-1, GIDUNG) not in answer and not ((x-1,y,BO) in answer and (x+1,y,BO) in answer) :
                return True
    return False
        
def solution(n, build_frame) :
    answer = set()

    for x, y, a, b in build_frame :
        if b :
            answer.add((x,y,a))
            if unavail(answer) :
                answer.remove((x,y,a))
        elif (x,y,a) in answer :
            answer.remove((x,y,a))
            if unavail(answer) :
                answer.add((x,y,a))
    
    answer = map(list, answer)

    return sorted(answer, key= lambda x : (x[0], x[1], x[2]))

n = 5
build = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build))

n = 5
build = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build))