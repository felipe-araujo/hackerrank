# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
input()
input()
input()

from math import erf, sqrt
def phi(x, mi, sigma):
    arg = (x-mi)/(sigma * sqrt(2))
    return 0.5 * ( 1 + erf(arg))

mean = 205
sigma = 15
n = 49

sigma2 = sigma * sqrt(n)
mean2 = mean * n

ans = phi(9800, mean2, sigma2)

print('{:.4f}'.format(ans))