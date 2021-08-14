# cook your dish here
T = int(input())
for _ in range(T):
    total_days, D, threshold = list(map(int, input().split()))
    total_per_day = list(map(int, input().split()))
    city_water_level = total_per_day[0]
    for i in total_per_day[1:]:
        if i == 0:
            city_water_level -= D
            city_water_level = max(city_water_level, 0)
        else:
            city_water_level += i
            if city_water_level > threshold:
                print("YES")
                break
    else:
        print("NO")
