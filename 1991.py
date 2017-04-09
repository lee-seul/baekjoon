# coding: utf-8


class BinaryTree:
    
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.data, end="")
        if self.right_child:
            self.right_child.inorder()

    def preorder(self):
        print(self.data, end="")
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.data, end="")


def return_None(e):
    if e == ".":
        return None
    return e

n = int(input())

stack = []
for _ in range(n):
    node = list(map(return_None, input().split()))
    stack.append(node)

dic = {}
while stack:
    node = stack.pop()
    key = node[0]
    dic[key] = BinaryTree(key)
    data = key
    if node[1] is None:
        left = None
    else:
        left = dic[node[1]]
    
    if node[2] is None:
        right = None
    else:
        right = dic[node[2]]

    dic[node[0]] = BinaryTree(data, left, right) 

root = dic['A']

root.preorder()
print()

root.inorder()
print()

root.postorder()
    

