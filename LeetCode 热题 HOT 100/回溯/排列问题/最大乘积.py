n = "123456789"

res = list()
temp = list()


def backtrace(index):
    if len(temp) > 0:
        res.append(''.join(temp[:]))

    for i in range(index, len(n)):
        temp.append(n[i])
        backtrace(i + 1)
        temp.pop()


backtrace(0)

for i in range(len(res)):
    for j in range(1, len(res[i])):
        if int(res[i][j]) - int(res[i][j - 1]) > 1:
            res[i] = 0
            break

maxNum = float("-inf")

for i in res:
    for j in res:
        if int(i) != 0 and int(j) != 0 and i != j:
                if maxNum < int(i) * int(j):
                    maxNum = int(i) * int(j)
print(maxNum)
