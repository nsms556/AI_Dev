class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def preorder(self):
        tr = []
        tr.append(self.data)
        
        if self.left :
            tr += self.left.preorder()
        if self.right :
            tr += self.right.preorder()

        return tr
    
class BinaryTree:

    def __init__(self, r):
        self.root = r


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


    def preorder(self):
        if self.root :
            return self.root.preorder()
        else :
            return []


def solution(x):
    return 0