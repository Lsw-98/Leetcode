"""

峰值元素是指其值大于左右相邻值的元素。
给你一个输入数组nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
你可以假设nums[-1] = nums[n] = -∞ 。

示例 1：
输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。

示例2：
输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5
解释：你的函数可以返回索引 1，其峰值元素为 2；
或者返回索引 5， 其峰值元素为 6。

"""


def findPeakElement(nums):
    if len(nums) < 2:
        return 0
    else:
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        else:
            for i in range(1, len(nums) - 1):
                if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                    return i


print(findPeakElement([1, 2, 3, 1]))
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))
