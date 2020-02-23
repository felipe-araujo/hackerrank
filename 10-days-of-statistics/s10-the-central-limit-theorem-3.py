# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
input()
input()
input()

from math import erf, sqrt
def phi(x, mi, sigma):
    arg = (x-mi)/(sigma * sqrt(2))
    return 0.5 * ( 1 + erf(arg))

mean = 500
sigma = 80
n = 100
z = 1.96

# sample mean
sigma2 = sigma / sqrt(n)
mean2 = mean 

A = mean2 - (z*sigma2)
B = mean2 + (z*sigma2)

print('{:.2f}'.format(A))
print('{:.2f}'.format(B))