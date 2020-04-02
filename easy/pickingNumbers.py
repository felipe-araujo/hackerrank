def pickingNumbers(a):
    # Write your code here    
    a.sort()
    print(a)
    diff = [abs(x-y) for x, y  in zip(a[0:-1], a[1:])]
    print(diff)
    diff = list(map(lambda x: 1 if x>=1 else 0, diff))
    print(diff)
    diff = str(diff).replace('[', '').replace(']', '').replace("'", '').replace(",", '').replace(" ", '')
    
    # longest zero sequence
    zeros = diff.split('1')
    zeros = list(map(lambda  x: len(x), zeros))
    zeros.sort()
    long_zero = zeros[-1]

    print(long_zero)

    ones = diff.split('0' * long_zero)
    ones = ones[1:]
    ones = list(map(lambda x: x.split('0')[0], ones))
    ones = list(map(lambda x: len(x), ones))
    ones.sort()

    print(diff)
    diff = diff.split('0')
    diff = list(map(lambda x: len(x), diff))
    diff.sort()
    return long_zero + ones[-1]

print(pickingNumbers([4, 6, 5, 3, 3, 1]))