"""

给定一个整数数组，找出总和最大的连续数列，并返回总和。

示例：
输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。

"""


def maxSubArray(nums):
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
    return max(dp)