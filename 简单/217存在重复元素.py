"""

给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

"""


def containsDuplicate(nums):
    new_nums = set(nums)
    if len(new_nums) < len(nums):
        return True
    else:
        return False


print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
