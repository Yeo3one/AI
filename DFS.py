graph = dict()

# graph 딕셔너리 ["Key"] = ["Value"]
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

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbor in graph[node]:
                stack.append(neighbor)

    print("DFS 알고리즘을 통해 방문한 모든 노드는 다음과 같다.")
    print(visited)

dfs(graph, "A")