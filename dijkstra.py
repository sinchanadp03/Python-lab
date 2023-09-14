#Develop an optimal route for a scenario where a person wants to buy a ticket to a baseball game.
#Along the way from house to reaching the destination, some known person who lives on that street might give money. 
#Visit towns for the collection of more money to buy a ticket.

import heapq
def dij(graph,start):
    distances={node:float('inf') for node in graph} 
    distances[start]=0
    heap=[(0,start)]
    while heap:
        currentdist,currentnode=heapq.heappop(heap)
        if currentdist>distances[currentnode]:
            continue
        for neighbor,weight in graph[currentnode].items():
            distance=currentdist+weight
            if distance<distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(heap,(distance,neighbor))
    return distances
def optimal(graph,start,dest):
    distances=dij(graph,start)
    if distances[dest]==float('inf'):
        return None
    route=[]
    node=dest
    while node!=start:
        route.append(node)
        neighbors=graph[node]
        min=float('inf')
        nextN=None
        for neighbor,weight in neighbors.items():
            if distances[neighbor]+weight==distances[node] and distances[neighbor]<min:
                min=distances[neighbor]
                nextN=neighbor
        if nextN is None or nextN in route:
            return None
        node=nextN
        
    route.append(start)
    route.reverse()
    return route
graph = {
    'A': {'B': 3, 'C': 99, 'D': 7, 'E': 99},
    'B': {'A': 3, 'C': 4, 'D': 2, 'E': 99},
    'C': {'A': 99, 'B': 4, 'D': 5, 'E': 6},
    'D': {'A': 7, 'B': 2, 'C': 5, 'E': 4},
    'E': {'A': 99, 'B': 99, 'C': 6, 'D': 4}
}

start='A'
dest='E'
optimalroute=optimal(graph,start,dest)

if optimalroute is None:
    print("No")
else:
    print("Route is",'->'.join(optimalroute))
