"""

编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，
也可能是 无限循环 但始终变不到 1。如果 可以变为 1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

示例：
输入：19
输出：true
解释：
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1

"""


def isHappy(n):
    used = []
    while n != 1:
        if n in used:
            return False
        used.append(n)
        temp = list(str(n))
        temp_sum = 0
        for i in range(len(temp)):
            temp_sum += int(temp[i]) ** 2
        n = temp_sum
    return True

    # mem = set()  # 利用 set（）集合，保存平方求和后的数值
    #     while n != 1:  # 利用 while 实现循环
    #         n = sum([int(i) ** 2 for i in str(n)])  # 通过str（n）调取输入整数各个位数的值
    #         if n not in mem:  # 若平方求和后的数值是首次出现，则添加进集合中
    #             mem.add(n)
    #         else:  # 若求和后数值，在集合中存在，则直接返回false,即出现死循环
    #             return False
    #     return True  # 最终当n==1时，跳出while循环，返回true


print(isHappy(19))
