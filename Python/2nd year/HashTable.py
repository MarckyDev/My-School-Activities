# HashTable
# HashTable is based on the ide of hash Functions
# Hash Functions may data or value tas itatranslate yung data mo into a hash value
# Key - Pair Value ('a', maps to the value of 1)
# Hash the value of A then it will give the index it contains
#####################################
# STEPS
####################################
# 1.) Initialize a fixed Array [limited size array]
# ex.
# -> [null, null, null] <- 3 packets
####################################
# 2.) Node Data Structure
# -> Has Value
# -> pointer to the next node
# -> stores the key of the data
# makes a linked list to avoid collisions
# same hash of 1
# [null, data, null] -> [null, {node1 -> node2} <- a collision, null]
###################################
# 3.) Operation
# -> set value
# -> get value using a key
# -> traverse
# -> delete

# used for linkedlist buk=cket to handle has collision
class Node:
    def __init__(self, key, value) -> None:
        self.key = key # holds the key
        self.value = value # holds the value
        self.next = None # if none then it's the last node of your linked list


    def __str__(self) -> str:
        return f'<{self.key}-{self.value}> -> {self.next}'
    

    
class HashTable:
    def __init__(self, size) -> None:
        self.capacity = size
        self.table = [None for _ in range(size)]

    
    def _hash(self, key):
        return hash(key)%self.capacity
    
    def get(self, key):
        hashed = self._hash(key)
        # get from bucket
        bucket = self.table[hashed]
        #if yung bucket is not none
        if bucket is not None:

            node = bucket
            while node.next is not None:#hanapin kung yun yung actual key na want mong hanapin
                if node.key == key:
                    return node.value
                node = node.next
            else:
                return node.value
        return None
    def set(self, key, value):
        # hash the key -> returns integer
        # insert at table
        # if an index has value
        # it should insert the value to the linked list in that bucket to handle collision
        # key can be int, float, string, and boolean
        hashed = self._hash(key)
        if self.table[hashed] is None:
            # no value on that index yet
            self.table[hashed] = Node(key, value)
        else: # kung may value
            node = self.table[hashed]
            while node.next is not None: # traverses the linked list until mareach ang dulo
                node = node.next # gets the next node
            node.next = Node(key, value) # pag nareach na, iinsert lang yung bagong value


    def traverse(self, callback): # traverses through the hashtable and performs call back for each element

        pass

    def delete(self, key):
        # same as get but instead of returning the node
        # idedelete naten yung node
        hashed = self._hash(key)
        # get from bucket
        bucket = self.table[hashed]
        #if yung bucket is not None
        if bucket is not None:
            node = bucket
            prev_node = None
            
            while node.next is not None:
                # previous node will b
                # if yung current node is equal sa key
                if node.key == key:
                    #tanggalin yung pointer yung prev_node is popoint sa current next
                    prev_node.next = node.next
                    if prev_node is None:
                        # nasa start yung gusto nating idelete
                        # gagawan naten ng isa pang variable na ipopoint naten sa next node
                        # ng current node
                        self.table[hashed] = node.next
                        return
                    prev_node = node.next
                    return 
                prev_node = node
                node = node.next
            else:
                self.table[hashed] = None
        return None
        

    
    
    def __str__(self) -> str:
        return str([str(x) for x in self.table])




hashTable = HashTable(5)

hashTable.set(5, 10) # 5%5 = 0
hashTable.set(10, 2) # 10%5 = 0
hashTable.set('hi', 'hello')# nagiiba ang hash value depending sa seed mo, based on sessions ng program mo
 
print(hashTable)
print(hashTable.get(10)) # lalabas dito ay 2
print(hashTable.get('hi')) # lalabas dapat dito ay hello
# deletes
hashTable.delete(10)
print(hashTable)