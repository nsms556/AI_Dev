def solution(participant, completion):
    count = {}

    for people in participant :
        count[people] = count.get(people, 0) + 1

    for people in completion :
        count[people] -= 1

    retire = [k for k,v in count.items() if v != 0]

    return retire[0]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))