# cook your dish here
Q = int(input())
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    T = list(map(int, input().split()))
    index = list(range(1, N + 1))
    z = list(map(lambda z, x, y: [z, x, y], index, A, T))
    z.sort(key=lambda x: x[1])
    ans = []
    tot = 0
    for i in range(N):
        if z[i][1] > z[i][2]:
            continue
        if z[i][1] + tot <= z[i][2]:
            ans.append(z[i])
            tot += z[i][1]
    ans.sort(key=lambda x: x[2])
    print(len(ans), end=" ")
    tot = 0
    for i in range(len(ans)):
        if i % 3 == 0:
            print()
        print(ans[i][0], " ", tot, " ", ans[i][2] + tot)
        tot += ans[i][2] + tot
    print()

# # cook your dish here
# Q = int(input())
# for _ in range(Q):
#     N = int(input())
#     A = list(map(int,input().split()))
#     T = list(map(int,input().split()))
#     index = list(range(1,N+1))
#     z = list(map(lambda z,x,y: [z,x,y],index,A,T))
#     z.sort(key=lambda x: x[1])
#     ans = []
#     tot = 0
#     for i in range(N):
#         if z[i][1]>z[i][2]:
#             continue
#         if z[i][1]+tot<=z[i][2]:
#             ans.append(z[i][0])
#             ans.append(tot)
#             ans.append(z[i][1]+tot)
#             tot+=z[i][1]
#     print(len(ans)//3,end=" ")
#     for i in range(len(ans)):
#         if i%3 ==0:
#             print()
#         print(ans[i],end=" ")
#     print()