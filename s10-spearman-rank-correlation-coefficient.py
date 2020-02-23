# Enter your code here. Read input from STDIN. Print output to STDOUT
n = float(input())
X = list(map(float, input().strip().split()))
Y = list(map(float, input().strip().split()))

X_ord = sorted(X)
Y_ord = sorted(Y)

X_rank = map(lambda x: X_ord.index(x)+1, X)
Y_rank = map(lambda y: Y_ord.index(y)+1, Y)
for k in range(0, len(X)):
    rank_x = X_ord.index(X[k])

d2 = 0
for rx, ry in zip(X_rank, Y_rank):
    d2 += (rx-ry)*(rx-ry)

num = 6*d2
den = n*(n*n -1)
ro = 1 - (num/den)

print('{:.3f}'.format(ro))