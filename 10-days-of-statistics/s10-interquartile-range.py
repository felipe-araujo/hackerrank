# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()

def str_to_list(string):
    return list(map(int, string.strip().split()))

elements = str_to_list(input())
frequencies = str_to_list(input())

S = []
for el, freq in zip(elements, frequencies):
    S += [el] * freq

def median(arr):
    med = None
    k = int(len(arr)/2)
    if len(arr) % 2 ==0:
        med = (arr[k-1] + arr[k])/2
    else:
        med = arr[k]
    return med

S.sort()

k = int(len(S)/2)
L = None
U = None
if len(S) % 2 == 0:
    L = S[0:k]
    U = S[k:]
else:
    L = S[0:k]
    U = S[k+1:]

q1 = median(L)
q2 = median(S)
q3 = median(U)

print('{:.1f}'.format(q3-q1))
