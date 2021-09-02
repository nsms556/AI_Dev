# 0831 호텔 방 배정
# https://programmers.co.kr/learn/courses/30/lessons/64063

import sys
sys.setrecursionlimit(10 ** 6)

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
