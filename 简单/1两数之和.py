"""

给定一个整数数组 nums和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""


def twoSum(lst, target):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            sum = lst[i] + lst[j]
            if sum == target:
                return i, j


# print(twoSum([2, 7, 11, 15, 21], 13))
# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
# print(twoSum([-1, 0], -1))
# print(twoSum([0, 0, 3, 4], 0))
