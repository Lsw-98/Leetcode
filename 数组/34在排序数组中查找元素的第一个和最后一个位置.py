"""

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回[-1, -1]。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

"""


def searchRange(nums, target):
    ans = []
    low = 0
    high = len(nums) - 1
    low_flag = True
    high_flag = True
    while low < len(nums) or high >= 0:
        if nums[low] == target and low_flag:
            ans.append(low)
            low_flag = False
        if nums[high] == target and high_flag:
            ans.append(high)
            high_flag = False
        low += 1
        high -= 1
    ans.sort()
    if not ans:
        ans.append(-1)
        ans.append(-1)
    return ans


print(searchRange([5, 7, 7, 8, 8, 10], 8))
print(searchRange([5, 7, 7, 8, 8, 10], 6))
print(searchRange([], 0))
print(searchRange([1], 1))
