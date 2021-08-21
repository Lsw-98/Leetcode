"""

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释:连续子数组[4,-1,2,1] 的和最大，为6。

"""


def maxSubArray(nums):
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
    return max(dp)