# code
def calcSum(s1, s2):
    first = s2
    second = s1
    if len(s1) > len(s2):
        first = s1
        second = s2

    res = list()
    n1 = len(first)
    n2 = len(second)
    carry = 0
    for i in range(1, len(first) + 1):

        if len(second) >= i:
            s = first[-i] + second[-i] + carry

        else:
            s = first[-i] + carry

        if s < 2:
            carry = 0
            res.append(s)
        else:
            carry = 1
            if s == 2:
                res.append(0)
            if s == 3:
                res.append(1)

    if carry:
        res.append(1)

    l = list()
    for d in reversed(res):
        l.append(d)

    return l


s1_input = '1101 111'
s2_input = '10 01'
s1 = [int(d) for d in s1_input if d !=' ']
s2 = [int(d) for d in s2_input if d !=' ']
print(*calcSum(s1, s2))

s1_input = '1101'
s2_input = '111'
s1 = [int(d) for d in s1_input if d !=' ']
s2 = [int(d) for d in s2_input if d !=' ']
print(*calcSum(s1, s2))

s1_input = '10'
s2_input = '01'
s1 = [int(d) for d in s1_input if d !=' ']
s2 = [int(d) for d in s2_input if d !=' ']
print(*calcSum(s1, s2))



s = list(map(int, s1_input.rstrip().split()))
