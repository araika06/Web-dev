n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    if int(arr[i])*int(arr[i-1]) > 0:
        print("YES")
        break
else:
    print("NO")


