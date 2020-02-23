# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()

from math import exp, pow
def fat(x):
    f = 1
    for i in range(2, x+1):
        f = f*i
    return f

def p(k, lambd):
    return (pow(lambd, k) * exp(-lambd)) / fat(k)

ans = p(5, 2.5)

print('{:.3f}'.format(ans))