class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
    def print(self, node=None):
        if not node:
            node = self.root
        if node.left:
            self.print(node.left)
        #print( "[", str(node) , "left=", str(node.left),"right=", str(node.right), "]")
        print(node)
        if node.right:
            self.print(node.right)


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def iterate(node, covered_l, covered_r, current_distance, delta, nodes_l, nodes_r):
    dr = None
    dl = None
    if node.right:
        dr = current_distance + delta/2
    if node.left:
        dl = current_distance - delta/2
    
    if dr and dr > covered_r:
        covered_r = current_distance + delta
        nodes_r.append(node.right)
        
    dr = current_distance + delta/2

    if dl and dl < covered_l:
        covered_l = current_distance - delta
        nodes_l.append(node.left)
    
    dl = current_distance - delta/2
    
    if node.right:
        iterate(node.right, covered_l, covered_r, dr, delta, nodes_l, nodes_r)
    if node.left:
        iterate(node.left, covered_l, covered_r, dl, delta, nodes_l, nodes_r)
    return nodes_l, nodes_r
        


def topView(root):
    if not root:
        return
    view = []
    node = root
    partial_left = []
    
    # right side of the tree
    node = root
    covered_l = 0
    covered_r = 0
    current = 0 # D
    d = 8
    l, r = iterate(root, covered_l, covered_r, current, d, [], [])


    view = list(reversed(l)) + [root.info] + r
    view = list(map(str, view))
    print(' '.join(view))
    #Write your code here



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])
#tree.print()

topView(tree.root)