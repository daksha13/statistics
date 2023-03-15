# c. To explore the library which helps to traverse the directed and undirected graph.

from igraph import *

g = Graph()

g.add_vertices(7)

g.add_edges([(0, 1), (1, 2), (4, 5), (2, 3), (1, 3), (5, 6), (3, 4)])

g.delete_edges(5)
print(g)
print()

g.delete_vertices(2)
print(g)

'''# BFS

graph = {
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': ['F'], 
    'F': []
}

visited = []
queue = []

def bfs(v, graph, n):
    v.append(n)
    queue.append(n)

    while queue:
        s = queue.pop(0)
        print(s, end = " ")

        for neighbour in graph[s]:
            if neighbour not in v:
                v.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, 'B')



# DFS

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()

def dfs(v, graph, n):
    if n not in v:
        print(n)
        v.add(n)
        for neighbour in graph[n]:
            dfs(v, graph, neighbour)

dfs(visited, graph, 'A')
'''