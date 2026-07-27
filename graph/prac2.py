#1971 find if path exists in graph
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        # Build the graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize BFS
        queue = deque([source])
        visited = {source}

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return False