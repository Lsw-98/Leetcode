"""

给定一个包含n + 1 个整数的数组nums ，其数字都在 1 到 n之间（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3

示例 3：
输入：nums = [1,1]
输出：1

示例 4：
输入：nums = [1,1,2]
输出：1

"""


def findDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]


print(findDuplicate([1, 3, 4, 2, 2]))
print(findDuplicate([3, 1, 3, 4, 2]))
print(findDuplicate([1, 1]))
print(findDuplicate([1, 1, 2]))
