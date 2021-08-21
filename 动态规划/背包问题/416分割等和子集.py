"""

给你一个 只包含正整数 的 非空 数组nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。

"""


def canPartition(nums):
    values = nums[:]
    weights = nums[:]
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    res = sum(nums) // 2
    for i in range(1, n):
        for j in range(1, n):
            # dp[i - 1][j - weight[i]] + value[i]
            # 由dp[i - 1][j - weight[i]]推出，dp[i - 1][j - weight[i]] 为背包容量为j - weight[i]的时候不放物品i的最大价值，
            # 那么dp[i - 1][j - weight[i]] + value[i] （物品i的价值），就是背包放物品i得到的最大价值
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])
            if dp[i][j] == res:
                return True
    return False


print(canPartition([1, 5, 11, 5]))
print(canPartition([1, 2, 3, 5]))
