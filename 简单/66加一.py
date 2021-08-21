"""

给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]

"""


def plusOne(lst):
    sum = int(''.join(map(str, lst)))
    sum += 1
    newlst = []
    while sum != 0:
        newlst.append(sum % 10)
        sum //= 10
    if len(lst) > len(newlst):
        for i in range(len(lst) - len(newlst)):
            newlst.append(0)
    newlst.reverse()
    return newlst
