q = 1
adnx = [1, 1, 3000, 100000000]

#q = int(input())
#adnx = list(map(int, input().strip().split()))

a = adnx[0]
d = adnx[1]
n = adnx[2]
x = adnx[3]

cn = a - n*d
c1 = d + x
c0 = d - a - x

coef = [cn] + ([d] * (n-2)) + [c1, c0]

from math import pow
def f2(coef, x):
    sum = coef[-1]
    xn = x
    for c, p in zip(reversed(coef[0:-1]), range(1, len(coef))):
        sum += xn * c
        xn = xn * x    
    return sum

from math import pow
def f(r):
    rn = pow(r, n)
    return (cn * rn) + (d*(rn - r*r)/(r-1)) + r*c1 + c0

def df(r):
    rn_1 = pow(r, n-1)
    term00 = n*rn_1*cn
    term01 = c1
    term02 = d*((n*rn_1 - 2*r)*(r-1) - (rn_1*r - r*r))/((r-1)*(r-1))
    return term00 + term01 + term02

def find_root(coef):
    expo_minus_one = [c-1 for c in coef][0:-1]
    deriv = []
    n = len(expo_minus_one)
    for c, e in zip(coef[0:-1], range(n-1, -0, -1)):
        deriv.append(c*e)

    #print('coef:', coef)
    #print('deriv:', deriv)

    guess = 1.1
    for _ in range(0, 100000):
        guess = guess - (f(guess)/df(guess))
    return guess

def test_poly():
    # 2x + 1
    poly01 = [2, 1]
    print('should be 3', f(poly01, 1))
    # 3x² + 2x    12 + 4
    poly02 = [3, 2, 0]
    print('should be 16', f(poly02, 2))


def main2():
    import time
    t = time.process_time()
    ans = find_root(coef)
    elapsed_time = time.process_time() - t
    print('{:.14f}'.format(ans))
    print('1.00136521495144 (expected) ')    
    print('Time elapsed: ', elapsed_time)
    print('Previous time was ~ 5.7s')

    

def main():
    ans = find_root(coef)
    print('{:.12f}'.format(ans))

main2()



