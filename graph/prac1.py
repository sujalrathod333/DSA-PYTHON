from collections import deque

def bfs(graph, start, n):
    visited = [False]*n
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        print(node, end="-> ")
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

graph = {
    0: [1, 2],   # A -> B, C
    1: [3, 4],   # B -> D, E
    2: [5],      # C -> F
    3: [],
    4: [],
    5: []
}

print(bfs(graph, 2, 6))