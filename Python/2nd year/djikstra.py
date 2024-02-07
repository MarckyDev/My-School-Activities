from heapq import heapify, heappush, heappop
import sys

slay = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 3, 'D': 1},
    'C': {'A': 1, 'B': 3, 'D': 4},
    'D': {'B': 1, 'C': 4},
    'E': {'C': 2, 'F':1},
    'F': {'A': 5, 'E':1}
}

# (start, end, distance)
# 1st step find adjacent node
# 2nd, find the value of each kapitbahay
def dijkstra(graph, start, end):
    # initialize an infinite value
    infinite = sys.maxsize

    nodes = {
        'A': {'value': infinite, 'kapitbahay':[]},
        'B': {'value': infinite, 'kapitbahay':[]},
        'C': {'value': infinite, 'kapitbahay':[]},
        'D': {'value': infinite, 'kapitbahay':[]},
        'E': {'value': infinite, 'kapitbahay':[]},
        'F': {'value': infinite, 'kapitbahay':[]}
        }
    
    # reassigned into 0
    nodes[start]['value'] = 0

    # keeps track of the binisita notes
    binisita = []    

    # stores the start node into a buffer so that it gets priority
    temp = start
    
    # iterates throughout the whole graph
    for i in range(len(graph)):

        if temp not in binisita:
            # visits this node
            binisita.append(temp)
            minimum_heap = []

            # finds the neighbors of the temp variable
            # find out which of the neighbors have the smallest value
            for kapit_bahay in graph[temp]:
                if kapit_bahay not in binisita:
                     
                    # this will calculate the distance between nodes
                    value = nodes[temp]['value'] + graph[temp][kapit_bahay]
                    
                    # assign the value but first, compare
                    if value < nodes[kapit_bahay]['value']:
                        nodes[kapit_bahay]['value'] = value

                        # calculate the neighbors' value
                        nodes[kapit_bahay]['kapitbahay'] = nodes[temp]['kapitbahay'] + [temp]

                    # it creates a heap then stores all the data in the heap and their neighbors
                    heappush(minimum_heap, (nodes[kapit_bahay]['value'], kapit_bahay))

            heapify(minimum_heap)

            # 1 represents the neighboring element
            # checks first the minimum_heap list if it has content then,
            if len(minimum_heap) > 0:
                # if minimum_heap has elements in it, it gets popped
                temp = heappop(minimum_heap)[1]

    print("Shortest Distance: " + str(nodes[end]['value']))
    print("Shortest Path: " + str(nodes[end]['kapitbahay'] + [end]))

dijkstra(slay, 'A', 'D')