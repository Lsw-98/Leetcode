"""

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

"""


def moveZeroes(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        if nums[low] == 0:
            del nums[low]
            nums.append(0)
            high -= 1
        else:
            low += 1
    return nums


print(moveZeroes([0, 1, 0, 3, 12]))
