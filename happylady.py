def happyLadybugs(b):
    if len(b) < 2:
        return 'NO'
    if len(b) == 2:
        if b[0] == b[1]:
            return 'YES'
        else:
            return 'NO'

    if '_' not in b:
        if b[0] != b[1] or b[-1] != b[-2]:
            return 'NO' 
        for i in range(1, len(b)-1):
            if b[i-1] != b[i] and b[i] !=b[i+1]:
                return 'NO'
            else:
                return 'YES'
    else:
        c = {}
        for el in b:
            if el == '_':
                continue
            if el not in c:
                c[el] = 1
            else:
                c[el] = c[el] + 1
        for k in c:
            if c[k] < 2:
                return 'NO'
        return 'YES'

inputs = ['G', 'GR', '_GR_', '_R_G_', 'R_R_R', 'RRGGBBXX', 'RRGGBBXY']
for i in inputs:
    print('input:', i)
    print(happyLadybugs(i))
