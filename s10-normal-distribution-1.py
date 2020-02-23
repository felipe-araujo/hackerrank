# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
from math import erf, sqrt

def phi(x, mi, sigma):
    arg = (x-mi)/(sigma * sqrt(2))
    return 0.5 * ( 1 + erf(arg))

mi = 20
sigma = 2
ans1 = phi(19.5, mi, sigma)
ans2 = phi(22, mi, sigma) - phi(20, mi, sigma)

print('{:.3f}'.format(ans1))
print('{:.3f}'.format(ans2))