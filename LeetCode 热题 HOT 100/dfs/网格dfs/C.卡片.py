n = 1
nums = [i for i in range(1, n // 2 + 1)]
temp = []
res = []

for x in range(1, n // 2 + 1):
    y = 1
    while y <= x:
        res.append([y, x])
        y += 1

print(res)
