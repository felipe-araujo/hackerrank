nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]

data = list(map(int, input().split()))


"""The naive solution
"""
def naive(data):
    for _ in range(m):
        query = input().split()
        if query[0] == '1':
            i = int(query[1])
            j = int(query[2])
            shift = data[i-1:j]
            data = shift + data[:i-1] + data[j:]
            
        else:
            i = int(query[1])
            j = int(query[2])
            shift = data[i-1:j]
            data = data[:i-1] + data[j:] + shift
    print(abs(data[0] - data[-1]))
    print(" ".join(map(str, data)))

"""Instead of moving the elements,
 try keeping an array u[i]
 where u[i] = final position of element i
 in original array after all operations.
"""
def version01(data):
    idx = list(range(len(data)))
    idx = [0] * len(data)
    for _ in range(m):
        query = input().split()
        if query[0] == '1':
            offset = len(data[:i-1])
            idx[i-1] -= offset
            idx[j] += offset
            #if offset
            i = int(query[1])
            j = int(query[2])
            shift = data[i-1:j]
            data = shift + data[:i-1] + data[j:]
            
        else:
            i = int(query[1])
            j = int(query[2])
            shift = data[i-1:j]
            data = data[:i-1] + data[j:] + shift
    print(abs(data[0] - data[-1]))
    print(" ".join(map(str, data)))

"""Reverse transformations keeping track 
of index of start and end of array. 
"""
def op01(data, start, end):
    target = 0
    for target in range(len(data)):
        if target >= end:
            #return target
            pass
        elif target >= start-1 and target < end:
            #return target - (start-1)
            data[target] = target - (start-1)
        else:
            data[target] = target + (end-start+1)
            #return target + (end-start+1)

def op02(data, start, end):
    size = len(data)
    for target in range(len(data)):
        if target < start-1:
            pass
            #return target
        elif target >= start-1 and target < end:
            data[target] = target + (size-end)
            #return target + (size-end)
        else:
            data[target] = target - (end+start+1)
            #return target - (end+start+1)
    

def version02(data):
    size = len(data)
    idx = list(range(len(data)))
    print('m=', m)    
    for it in range(m):
        if it % 1000 == 0:
            print('Iteration #', it)
        query = input().split()
        i = int(query[1])
        j = int(query[2])
        if query[0] == '1':
            #pass
            op01(data, i, j)
            #idx = map(lambda x: op01(x,i,j), idx)            
        else:
            #pass
            op02(data, i, j)
            #idx = map(lambda x: op02(x,i,j,size), idx)
    idx = list(idx)
    a1 = data[idx[0]]        
    an = data[idx[-1]]        
    print(abs(data[0] - data[-1]))
    #print(" ".join(map(str, data)))

class Node:
    def __init__(self, start, end):
        self.prev = None
        self.next = None
        self.start = start
        self.end = end

    def __str__(self):
        return "[start={}, end={}]".format(start, end)

"""Tries to keep track of index changes, not
values. 
Uses a running sum scheme.
"""
def version03(data):
    size = len(data)
    tracker = Node(0, size)
    
    
    idx = [0] * size
    for _ in range(m):
        query = input().split()
        i = int(query[1])
        j = int(query[2])
        if query[0] == '1':
            start = 0
            end = None
            current = tracker
            while current:
                end = start + (current.end - current.start)
                current = current.next

            pass
            
        else:
            #pass
            idx = map(lambda x: op02(x,i,j,size), idx)
    idx = list(idx)
    a1 = data[idx[0]]        
    an = data[idx[-1]]        
    print(abs(data[0] - data[-1]))
    print(" ".join(map(str, data)))

version02(data)

