def gongyue(a, b):
    while(b != 0):
        temp = a % b
        a = b
        b = temp
    return int(a)


def gongbei(a, b):
    return int(a * b / gongyue(a, b))


print(gongbei(15, 25))
