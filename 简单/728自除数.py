"""

自除数是指可以被它包含的每一位数除尽的数。
例如，128 是一个自除数，因为128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
还有，自除数不允许包含 0 。
给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

示例 1：
输入：
上边界left = 1, 下边界right = 22
输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

"""


def selfDividingNumbers(left, right):
    ans = list()
    for i in range(left, right + 1):
        temp = list(map(int, str(i)))
        temp_j = -1
        for j in range(len(temp)):
            if temp[j] == 0:
                break
            if i % temp[j] != 0:
                break
            else:
                temp_j = j
        if temp_j == len(temp) - 1:
            ans.append(i)
    return ans


print(selfDividingNumbers(1, 22))
