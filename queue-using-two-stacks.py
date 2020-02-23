# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
l0 = []
l1 = []
for _ in range(n):
    args = input().split()
    if args[0] == '1':        
        v = int(args[1])
        if l0:            
            for t in range(len(l0)):
                l1.append(l0.pop())
            l1.append(v)
        elif not l0:            
            l1.append(v)        
    elif args[0] == '2':
        if l0:
            l0.pop()
        elif l1:
            for t in range(len(l1)-1):
                l0.append(l1.pop())
            l1.pop()
    else:
        if not l0 and l1:
            for t in range(len(l1)):
                l0.append(l1.pop())
        if l0:
            print(l0[-1])
        
