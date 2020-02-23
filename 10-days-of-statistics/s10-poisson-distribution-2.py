# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
lambda1 = 0.88
lambda2 = 1.55
ans1 = 160 + 40*(lambda1 * (1+lambda1))
ans2 = 128 + 40*(lambda2 * (1+lambda2))

print('{:.3f}'.format(ans1))
print('{:.3f}'.format(ans2))