T = int(input())
for _ in range(T):
    problem_difficulties_list = list(map(int, input().split()))
    prob_unique_list = list(set(problem_difficulties_list))
    if len(prob_unique_list) > 2:
        print("2")
    elif len(prob_unique_list) > 1:
        print("1")
    else:
        print("0")


