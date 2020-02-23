# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
l0 = []
l1 = []
for _ in range(n):
    args = input().split()
    if args[0] == '1':
        v = int(args[1])
        for t in range(len(l0)):
            l1.append(l0.pop())
        l0.append(v)
        for t in range(len(l1)):
            l0.append(l1.pop())        
    elif args[0] == '2':
        l0.pop()
    else:
        print(l0[-1])
