from priorityQueue import PriorityQueue
#finds the least cost path from startingNode to targetNode 
def dijkstraSearch(app, graph, startingNode, targetNode):
    queue = PriorityQueue()
    queue.put(startingNode, 0)
    cameFrom = {}
    costSoFar = {}
    cameFrom[startingNode] = None
    costSoFar[startingNode] = 0

    while not queue.empty():
        current = queue.get()
        #for visualizer:
        app.dijkstraSearchQueue.append(current)
        ################
        if current == targetNode:
            return reconstructPath(cameFrom, startingNode, targetNode)
       
        for (neighborRow, neighborCol, weight) in graph[current]:
            neighborNode = (neighborRow, neighborCol)
            newCost = costSoFar[current] + weight
            if neighborNode not in costSoFar or newCost < costSoFar[neighborNode]:
                costSoFar[neighborNode] = newCost
                priority = newCost
                queue.put(neighborNode, priority)
                cameFrom[neighborNode] = current

    return None

def reconstructPath(cameFrom, startingNode, targetNode):
    current = targetNode
    path = []
    while current != startingNode:
        path.append(current)
        current = cameFrom[current]
    path.append(startingNode)
    path.reverse()
    return path
