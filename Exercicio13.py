a, b = 0, 1

for _ in range(16):
    a, b = b, a + b
    print(a)