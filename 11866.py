# coding: utf-8

class Node:
    def __init__(self, data, nextNode=None, preNode=None):
        self.data = data
        self.nextNode = nextNode
        self.preNode = preNode

    def set_next_node(self, nextNode, preNode):
        self.nextNode = nextNode
        self.preNode = preNode

n, m = map(int, input().split())

linked_list = [Node(i) for i in range(1, n+1)]
for i, data in enumerate(linked_list):
    if i == n-1:
        linked_list[i].set_next_node(linked_list[0], linked_list[i-1])
    elif i == 0:
        linked_list[i].set_next_node(linked_list[i+1], linked_list[n-1])
    else:
        linked_list[i].set_next_node(linked_list[i+1], linked_list[i-1]) 

result = []
startNode = linked_list[m-1]
while len(result) < n:
    result.append(str(startNode.data))
    startNode.preNode.nextNode = startNode.nextNode
    startNode.nextNode.preNode = startNode.preNode 
    for _ in range(m):
        startNode = startNode.nextNode
        
print("<" + ", ".join(result) + ">")
