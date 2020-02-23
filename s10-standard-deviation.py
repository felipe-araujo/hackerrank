from math import sqrt

_ = input()

def str_to_list(string):
    return list(map(int, string.strip().split()))

numbers = str_to_list(input())

mean = sum(numbers) / len(numbers)

sumdev = 0 
for n in numbers:
    sumdev += (n - mean)*(n - mean)

std = sqrt(sumdev / len(numbers))
print('{:.1f}'.format(std))