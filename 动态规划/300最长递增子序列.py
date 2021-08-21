"""

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1

"""


def lengthOfLIS(nums):
    # 3684ms
    # n = len(nums)
    # if n <= 1:
    #     return 1
    # else:
    #     dp = [1 for _ in range(n)]
    #     res = 0
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #         if dp[i] > res:
    #             res = dp[i]
    #     return res

    # 二分
    d = []
    for n in nums:
        if not d or n > d[-1]:
            d.append(n)
        else:
            l, r = 0, len(d) - 1
            loc = r
            while l <= r:
                mid = (l + r) // 2
                if d[mid] >= n:
                    loc = mid
                    r = mid - 1
                else:
                    l = mid + 1
            d[loc] = n
    return len(d)

    # dp
    # res = 0
    # n = len(nums)
    # dp = [1 for _ in range(n)]
    # for i in range(1, n):
    #     for j in range(i):
    #         if nums[i] > nums[j]:
    #             dp[i] = max(dp[i], dp[j] + 1)
    #     if dp[i] > res:
    #         res = dp[i]
    # return res


print(lengthOfLIS([4, 10, 4, 3, 8, 9]))
print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(lengthOfLIS([7, 7, 7, 7, 7, 7]))




