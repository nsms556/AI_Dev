def solution(max_weight, specs, names):
    dic = {}

    for item in specs :
        dic[item[0]] = int(item[1])

    weight = 0
    trucks = 1

    for name in names :
        if weight + dic[name] > max_weight :
            trucks += 1
            weight = dic[name]
        else :
            weight += dic[name]

    return trucks


a = 300
b = [["toy","70"], ["snack", "200"]]
c = ["toy", "snack", "snack"]
#c = ["toy", "snack", "toy"]

print(solution(a, b, c))