# Enter your code here. Read input from STDIN. Print output to STDOUT
# at least 3 boys: 3, 4, 5 or 6 out of 6
_ = input()
pboy = (1.09) / (1 + 1.09)
pgirl = 1 - pboy

def n_choose_x(n, x):
    f1 = 1
    for i in range(n, (n-x), -1):
        f1 = f1 * i
    f2 = 1
    for i in range(1, x+1):
        f2 = f2 * i
    return f1/f2

from math import pow
def pboys(x):
    return n_choose_x(6, x) * (pow(pboy, x)) * (pow(pgirl, 6-x))

answ = pboys(3) + pboys(4) + pboys(5) + pboys(6)
print('{:.3f}'.format(answ))