graph = {
    'A' : set(['B','C']),
    'B' : set(['A','D','E']),
    'C' : set(['A','F']),
    'D' : set(['B']),
    'E' : set(['B','F']),
    'F' : set(['C','E'])
    }

'''
def dfs(graph,start):
    visited,stack = set(),[start]
    while stack:
        print("Stack before is ",stack)
        vertex = stack.pop()
        if vertex not in visited :
            print("visited before is ",visited)
            print("vertex before is ",vertex)
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
            print("graph vertex  ",graph[vertex])
            print("visited after  ",visited)
            print("Diff of grp and ver  ",graph[vertex]-visited)
            print("Stack after is ",stack)
            print("\n")
    return visited

print(dfs(graph,'A'))
'''

def dfs_path(graph,start,goal):
    stack = [(start,[start])]
    while stack:
        print("Satck is ",stack)
        (vertex,path) = stack.pop()
        print("vertex before is ",vertex)
        
        print("graph vertex  ",graph[vertex])
        print("path before is ",path)
        print("difference  ",graph[vertex] -  set(path))
        for next in graph[vertex] -  set(path):
            if next == goal :
                print("next is ",next)
                yield path + [next]
            else:
                stack.append((next,path+[next]))
        print("\n")
l1 = list(dfs_path(graph,'A','E'))
print(l1)
            
    
