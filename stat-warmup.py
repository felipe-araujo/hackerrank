# Enter your code here. Read input from STDIN. Print output to STDOUT
n = float(input())
numbers = list(map(int, input().strip().split()))

mean = sum(numbers)/n

numbers.sort()
median = 0
if n%2 == 0:
    median = (numbers[int(n/2) - 1] + numbers[int(n/2)])/2.0
else:
    median = numbers[int(n/2)]

mode = None
counter = dict()
for number in numbers:
    if number not in counter:
        counter[number] = 1
    else:
        counter[number] +=1

for c in counter.keys():
    if not mode:
        mode = c
    if (counter[c] > counter[mode]) or (counter[c] == counter[mode] and c<mode):
        mode = c

from math import sqrt
sd = 0
for number in numbers:
    sd += (number - mean) * (number - mean)
sd = sqrt(sd/n)

ci = (1.96) * (sd/sqrt(n))

print('{:.1f}'.format(mean))
print('{:.1f}'.format(median))
print(mode)
print('{:.1f}'.format(sd))
print('{:.1f}'.format(mean - ci), '{:.1f}'.format(mean + ci))

