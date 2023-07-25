graph = {
    'A' : set(['B','C']),
    'B' : set(['A','D','E']),
    'C' : set(['A','F']),
    'D' : set(['B']),
    'E' : set(['B','F']),
    'F' : set(['C','E'])
    }
def bfs(graph,start):
    visited,queue = set(),[start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)
    return visited

#print(bfs(graph,'A'))

def bfs_paths(graph,start,goal):
    queue = [(start,[start])]
    
    while queue :
        print("Queue is ",queue)
        (vertex,path) = queue.pop(0)
        print("vertex is ",vertex)
        print("path is ",path)
        print("graph vertex is ",graph[vertex])
        print("setpath is ",set(path))
        print("Diff of gv and setpath is ",graph[vertex] - set(path))
        for next in graph[vertex] - set(path):
            
            if next == goal:
                yield path + [next]
                print("if next is ", path + [next])
            else:
                print("Queue insertiom ",(next,path+[next]))
                queue.append((next,path+[next]))
      
        print("\n")      
print(list(bfs_paths(graph,'A','F')))

def shortest_path(graph,start,goal):
    try:
        return next(bfs_paths(graph,start,goal))
    except StopIteration:
        return None

print(shortest_path(graph,'A','F'))
