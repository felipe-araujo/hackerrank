# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for _ in range(0, n):
    number = input().strip()
    if re.match('^[7-9][\d]{9}$', number):
        print('YES')
    else:
        print('NO')
