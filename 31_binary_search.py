lst = [3, 4, 5, 6, 7, 8, 9]
x = 5
low = 0
high = len(lst)-1
for i in range(len(lst)):
    mid = (low + high)//2
    print("mid = ", mid)
    if x == lst[mid]:
        print(mid)
        break
    elif x > lst[mid]:
        low = mid + 1
        print("low = ", low)
    else:
        high = mid - 1
        print("high = ", high)
        print("************************")