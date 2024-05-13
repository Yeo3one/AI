graph = dict()

graph["A"] = ["B", "C"]
graph["B"] = ["D"]
graph["C"] = ["G", "H", "I"]
graph["D"] = ["E", "F"]
graph["E"] = []
graph["F"] = []
graph["G"] = []
graph["H"] = []
graph["I"] = ["J"]
graph["J"] = []

def bfs(graph, start_node):
    visited = []
    need_visit = []

    need_visit.append(start_node)

    count = 0

    while need_visit:
        count += 1
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(set(graph[node]))

    print("While 구문 반복 횟수는", count, "번 입니다.")
    return visited

print(bfs(graph, "A"))