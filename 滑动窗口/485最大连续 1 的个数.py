"""

给定一个二进制数组， 计算其中最大连续 1 的个数。

示例：

输入：[1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.

"""


def findMaxConsecutiveOnes(nums):
    n = len(nums)
    end = 0
    ans = 0
    count = 0
    while end < n:
        if nums[end] == 1:
            count += 1
            ans = max(count, ans)
        else:
            count = 0
        end += 1
    return ans


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
