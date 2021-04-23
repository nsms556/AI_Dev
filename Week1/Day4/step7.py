def solution(tickets):
    graph = {}

    for tk in tickets :
        graph[tk[0]] = graph.get(tk[0], []) + [tk[1]]
    for route in graph :
        graph[route].sort(reverse=True)

    stack = ['ICN']
    path = []

    while len(stack) > 0 :
        top = stack[-1]
        if top not in graph or len(graph[top]) == 0 :
            path.append(stack.pop())
        else :
            stack.append(graph[top][-1])
            graph[top] = graph[top][:-1]

    return path[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))