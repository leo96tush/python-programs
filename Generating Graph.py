from collections import defaultdict

graph = defaultdict(list)

def addedge(graph,u,v):
    graph[u].append(v)

def generate_edges(graph):
    edges = []

    for node in graph:
        for neighbor in graph[node]:
            edges.append((node,neighbour))

    return(edges)

