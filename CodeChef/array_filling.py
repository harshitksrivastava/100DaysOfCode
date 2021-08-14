import math

T = int(input())
for _ in range(T):
    n, m = list(map(int, input().split()))
    m_op = []
    print(n)
    print(m)
    for i in range(m):
        m_op.append(list(map(int, input().split())))
    m_op.sort(key=lambda x: x[0], reverse=True)
    i = 0
    temp = n
    res = 0
    diff = 1
    while i < len(m_op) and temp > 0:
        x, y = m_op[i]
        diff = (diff * y) // (math.gcd(diff, y))
        res += (temp - n // diff) * x
        temp = n // diff
        i += 1
    print(res)
