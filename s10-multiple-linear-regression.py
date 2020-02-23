# Enter your code here. Read input from STDIN. Print output to STDOUT
mn = list(map(int, input().strip().split()))
m = mn[0]
n = mn[1]

#print('m, n = ', m, n)

def str_to_list(string):
    return list(map(float, string.strip().split()))

X = []
Y = []
for i in range(0, n):
    numbers = str_to_list(input()) 
    X.append([1] + numbers[0:m])
    Y.append(numbers[m])
    

q = int(input())

Xp = []
for i in range(0, q):
    numbers = str_to_list(input()) 
    Xp.append([1] + numbers)


import numpy as np
X = np.array(X)
Y = np.array(Y)
arg0 = np.matmul(np.transpose(X), X)
arg1 = np.linalg.inv(arg0)

arg2 = np.matmul(np.transpose(X), Y)

# Normal equation: B = inv(X'*X) * X' * X
B = np.matmul(arg1, arg2)
#print('Shape of B', B.shape)
#print('B', B)

Xp = np.array(Xp)
#print('Shape of Xp', Xp.shape)

Yp = np.matmul(Xp, B)

for line in Yp:
    print('{:.2f}'.format(line))

