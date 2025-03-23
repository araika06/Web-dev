n = int(input())
arr = list(map(int, input().split()))

count = sum(1 for i in arr if i > 0)
print(count)