"""

我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。
请你返回由[low, high]范围内所有顺次数组成的 有序 列表（从小到大排序）。

示例 1：
输出：low = 100, high = 300
输出：[123,234]

示例 2：
输出：low = 1000, high = 13000
输出：[1234,2345,3456,4567,5678,6789,12345]

"""


def sequentialDigits(low, high):
    # 官方解题 O(1), 太牛逼了
    ans = list()
    for i in range(1, 10):
        num = i
        for j in range(i + 1, 10):
            num = num * 10 + j
            if low <= num <= high:
                ans.append(num)
    return sorted(ans)

    # 回溯
    # ans = list()
    # num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #
    # def backtrace(index, current):
    #     if low <= current <= high:
    #         ans.append(current)
    #
    #     for i in range(index, 9):
    #         if num[i] - current % 10 > 1 and current != 0:  # 判断前一位比后一位小1
    #             break
    #         temp = 10 * current + num[i]
    #         if temp <= high:
    #             backtrace(i + 1, temp)
    #
    # backtrace(0, 0)
    # return sorted(ans)


print(sequentialDigits(100, 300))
print(sequentialDigits(1000, 13000))
