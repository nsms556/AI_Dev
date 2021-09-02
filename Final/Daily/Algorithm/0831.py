def find(num, rooms) :
    if num not in rooms :
        rooms[num] = num + 1
        return num
    
    empty = find(rooms[num], rooms)
    rooms[num] = empty + 1

    return empty

def solution(k, room_number):
    answer = []
    rooms = {}

    for num in room_number :
        empty = find(num, rooms)
        answer.append(empty)

    return answer

k = 6
room = [1,3,4,1,3,1]

print(solution(k, room))

'''
1   1
    1->2
3   1 3
    1->2 3->4
4   1 3 4
    1->2 3->4->5
1   1 2 3 4
    1->2->3 3->4->5
3   1 2 3 4 5
    1->2->6 3->4->5->6
1   1 2 3 4 5 6
    1->2->6->7 3->4->5->7


'''