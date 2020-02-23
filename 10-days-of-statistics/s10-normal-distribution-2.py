# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
input()
input()

from math import erf, sqrt
def phi(x, mi, sigma):
    arg = (x-mi)/(sigma * sqrt(2))
    return 0.5 * ( 1 + erf(arg))

mi = 70
sigma = 10
ans1 = 1-phi(80, mi, sigma)
ans2 = 1-phi(60, mi, sigma)
ans3 = phi(60, mi, sigma)

print('{:2.2f}'.format(ans1*100))
print('{:2.2f}'.format(ans2*100))
print('{:2.2f}'.format(ans3*100))