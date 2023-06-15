# Using Depth First Search using the diagrammatic example that was given in class.

# Use adjacency list representation to represent the graph
graph = {
    "A" : ["B", "F", "H"], # root node
    "B" : ["C"],
    "C" : ["D"],
    "D" : ["E", "G"],
    "E" : ["F"],
    "F" : [],
    "G" : ["H"],
    "H" : []
}

# Using recursive approach

visited = set()

def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')