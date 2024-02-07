import heapq

class the_flying_huffmans:
    
    def __init__(self, frequency, character, left=None, right=None) -> None:
        self.frequency = frequency
        self.character = character

        # the directions where the letters will go
        self.left = left
        self.right = right

        # this is where the tree gets constructed
        self.tree = ' '
    
    def __lt__(self, next):
        return self.frequency < next.frequency


def printNode(node, value = ' '):
    new_value = value + str(node.tree)

    if(node.left):
        printNode(node.left, new_value + '0')
    if(node.right):
        printNode(node.right, new_value + '1')


    if(not node.left and not node.right):
        print("{} -> {}".format(node.character, new_value))

# THE WORD IS "HUFFMAN"

# letters : frequency
huffman_leaves = ['H', 'U', 'F', 'M', 'A', 'N']


frequencies = [1, 1, 2, 1, 1, 1]

# this is to store some of the nodes
nodes = []

for iterator in range(len(frequencies)):
    heapq.heappush(nodes, the_flying_huffmans(frequencies[iterator], huffman_leaves[iterator]))

while len(nodes) > 1:
    
    left_leaf = heapq.heappop(nodes)
    right_leaf = heapq.heappop(nodes)

    left_leaf.tree = 0
    right_leaf.tree = 1

    babyNode = the_flying_huffmans(left_leaf.frequency + right_leaf.frequency, 
                                   left_leaf.character + right_leaf.character, 
                                   left_leaf, 
                                   right_leaf)

    heapq.heappush(nodes, babyNode)

printNode(nodes[0])
