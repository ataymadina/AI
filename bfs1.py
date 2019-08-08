graph = {'A': ['B','C','D'],
         'B': ['E','F'],
         'C': ['G','H'],
         'D': ['I','J'],
         'E': [' '],
         'F': [' '],
         'G': [' '],
         'H': [' '],
         'I': [' '],
         'J': [' ']
        } 

def bfs(graph, start,goal):
    visited = []
    queue = [start]
 
    while queue:
        print(queue )
        #print( "queue {} , goal {}".format(queue,goal))
        if queue[0] == goal:
            node = queue.pop(0)
            visited.extend(node)
            break
        node = queue.pop(0)
        if node not in visited:
            if node == ' ':
                break
            visited.extend(node)
            neighbours = graph[node]
            for i in neighbours:
                if i != ' ':
                    queue.extend(i)
    return visited
 
print(bfs(graph,'A','F'))

