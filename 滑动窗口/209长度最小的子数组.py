"""

给定一个含有n个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。
如果不存在符合条件的子数组，返回 0

示例 1
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组[4,3]是该条件下的长度最小的子数组。

示例 2
输入：target = 4, nums = [1,4,4]
输出：1

示例 3
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

"""


def minSubArrayLen(target, nums):
    # 超时了
    # min = float("inf")
    # for i in range(1, len(nums) + 1):
    #     for j in range(len(nums)):
    #         temp = sum(nums[j:i + j])
    #         if temp >= target and len(nums[j:i + j]) < min:
    #             min = len(nums[j:i + j])
    # if min == float("inf"):
    #     return 0
    # else:
    #     return min

    # 滑动窗口法
    n = len(nums)
    ans = n + 1
    start, end = 0, 0
    total = 0
    while end < n:
        total += nums[end]
        while total >= target:
            ans = min(ans, end - start + 1)
            total -= nums[start]
            start += 1
        end += 1

    return 0 if ans == n + 1 else ans


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen(4, [1, 4, 4]))
print(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
print(minSubArrayLen(11, [1, 2, 3, 4, 5]))
print(minSubArrayLen(15, [1, 2, 3, 4, 5]))
