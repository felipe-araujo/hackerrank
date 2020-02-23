# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
# at least 3 boys: 3, 4, 5 or 6 out of 6
_ = input()

def n_choose_x(n, x):
    f1 = 1
    for i in range(n, (n-x), -1):
        f1 = f1 * i
    f2 = 1
    for i in range(1, x+1):
        f2 = f2 * i
    return f1/f2

from math import pow
def p_reject(x, p_incorrect):
    return n_choose_x(batch_size, x) * (pow(p_incorrect, x)) * (pow(1-p_incorrect, batch_size-x))

p_incorrect = 0.12
batch_size = 10
# no more than 2 rejects
answ1 = p_reject(0, p_incorrect) + p_reject(1, p_incorrect) + + p_reject(2, p_incorrect)

# at least 2 rejects
answ2 = 0
for r in range(2, batch_size+1):
    answ2 += p_reject(r, p_incorrect)


print('{:.3f}'.format(answ1))
print('{:.3f}'.format(answ2))