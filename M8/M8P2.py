a, b = 1, 1
print(a)
print(b)
for _ in range(18):
    a, b = b, a + b
    print(b)
