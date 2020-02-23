q = 1
adnx = [1, 1, 3000, 100000000]

#q = int(input())
#adnx = list(map(int, input().strip().split()))

a = adnx[0]
d = adnx[1]
n = adnx[2]
x = adnx[3]

cn1 = a - n*d
cn = a - n*d + d
c2 = -x
c1 = -a
c0 = a + x - d

from math import pow
def f(r):
    return cn1 * pow(r, n+1) + cn*pow(r, n) + (r*r*c2) + (c1*r) + c0

def df(r):
    return ((n+1)*cn1 * pow(r, n))+(n * pow(r, n-1) * cn) + (2*r*c2) + c1


def find_root():
    #expo_minus_one = [c-1 for c in coef][0:-1]
    #deriv = []
    #n = len(expo_minus_one)
    #for c, e in zip(coef[0:-1], range(n-1, -0, -1)):
    #    deriv.append(c*e)

    #print('coef:', coef)
    #print('deriv:', deriv)

    guess = 1.1
    for _ in range(0, 100000):
        guess = guess - (f(guess)/df(guess))
    return guess

def main2():
    import time
    t = time.process_time()
    ans = find_root()
    elapsed_time = time.process_time() - t
    print('{:.14f}'.format(ans))
    print('1.00136521495144 (expected) ')    
    print('Time elapsed: ', elapsed_time)
    print('Previous time was ~ 5.7s')

    

def main():
    ans = find_root(coef)
    print('{:.12f}'.format(ans))

main2()
