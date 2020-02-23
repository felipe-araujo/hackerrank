# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = input()
from math import pow
p = 1/3
n = 5

def g(n_, p_):
    return pow((1-p_), n_-1) * p_

ans = g(1, p) + g(2, p) + g(3, p) + g(4, p) + g(5, p)
print('{:.3f}'.format(ans))