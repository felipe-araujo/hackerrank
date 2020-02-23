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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    # brute force search for paths from root to a node
    def path_search(r, anode, path_so_far=[]):
        if not r:
            return []

        if r.info == anode:
            return path_so_far + [r]
        
        from_left = path_search(r.left, anode, path_so_far + [r])
        if from_left:
            return from_left
        from_right = path_search(r.right, anode, path_so_far + [r])
        if from_right:
            return from_right
        return []
    
    path_v1 = path_search(root, v1)
    path_v2 = path_search(root, v2)
    print('path_v1', path_v1)
    print('path_v2', path_v2)
    lca = None
    for p1, p2 in zip(path_v1, path_v2):
        if p1==p2:
            lca = p1
        else:
            break
    return lca


  #Enter your code here

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
