# T = int(input())
# for _ in range(T):
#     N, p, K = list(map(int, input().split()))
#     ans = []
#     for i in range(N):
#         ans.append((i, i % K))
#     ans.sort(key=lambda x: x[1])
#     day = 1
#     for i, j in ans:
#         if i == p:
#             print(day)
#             break
#         day += 1
#

T = int(input())
for _ in range(T):
    N, p, k = list(map(int, input().split()))
    x = (p % k) - 1
    y = (N - 1) - (((N - 1) // k) * k)
    day = 0
    if x > y:
        day = (y + 1) * (((N - 1) // k) + 1) + (x - y) * ((N - 1) // k)
    else:
        day = (x+1) * ((N - 1) // k+1)
    for i in range(x+1, N, k):
        day += 1
        if i == p:
            break
    print(day)
