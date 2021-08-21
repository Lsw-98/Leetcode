"""

给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组[4,-1,2,1] 的和最大，为 6

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [0]
输出：0

示例 4：
输入：nums = [-1]
输出：-1

示例 5：
输入：nums = [-100000]
输出：-100000

"""


def maxSubArray(nums):
    n = len(nums)
    max_num = float('-inf')
    add = 0
    for i in range(n):
        add += nums[i]
        max_num = max(max_num, add)
        if add < 0:
            add = 0
    return max_num


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([1]))
print(maxSubArray([0]))
print(maxSubArray([-1]))
print(maxSubArray([-10000]))
