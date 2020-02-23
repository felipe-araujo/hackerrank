
X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

mean_x = sum(X) /len(X)
mean_y = sum(Y) /len(Y)

num = 0
den = 0
for x, y in zip(X, Y):
    num += (x*y)
    den += (x*x)
num = num * len(X)
den = den * len(X)    
num = (num - (sum(X) * sum(Y)))
den = (den - (sum(X) * sum(X)))

b = num/den
a = mean_y - b*mean_x
ans = a+(b*80)

print('{:.3f}'.format(ans))