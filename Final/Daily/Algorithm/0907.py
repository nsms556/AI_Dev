# 0907 지형 이동
# https://programmers.co.kr/learn/courses/30/lessons/62050


def solution(land, height):
    answer = 0

    queue = []
    visit_list = []
    land_size = len(land)
    queue.append((0,0))

    for node in queue :
        print(node)
        visit_list.append(node)
        u = (node[0], max(0, node[1]-1))
        l = (max(0, node[0]-1), node[1])
        d = (node[0], min(land_size-1, node[1]+1))
        r = (min(land_size-1, node[0]+1), node[1])

        print(u, l, d, r)

    return u, l, d, r


if __name__ == '__main__ ' :
    land = [[1,  4,  8,  10], 
            [5,  5,  5,  5], 
            [10, 10, 10, 10], 
            [10, 10, 10, 20]]	
    height = 3

    print(solution(land, height))

    land = [[10, 11, 10, 11],
            [2,  21, 20, 10],
            [1,  20, 21, 11],
            [2,  1,  2,  1]]
    height = 1

    print(solution(land, height))