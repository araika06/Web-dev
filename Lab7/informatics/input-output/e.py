v = int(input())
t = int(input())

max_length = 109

position = (v * t) % max_length
print(position)