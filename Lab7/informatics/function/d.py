x = str(input())
d = str(input())

count = 0
for digit in x:
    if digit == d:
        count += 1

print(count)
