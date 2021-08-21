"""

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例1:
给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

示例2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

"""


# def removeDuplicates(nums):
#     new_nums = []
#     [new_nums.append(nums[i]) for i in range(len(nums)) if nums[i] not in new_nums]
#     del nums[:]
#     [nums.append(new_nums[j]) for j in range(len(new_nums))]
#     return len(nums)

#     new_nums = sorted(set(nums), key=nums.index)
#     del nums[:]
#     [nums.append(new_nums[j]) for j in range(len(new_nums))]
#     return len(nums)


def removeDuplicates(nums):
    import numpy as np
    new_nums = list(np.unique(nums))
    [nums.insert(i, new_nums[i]) for i in range(len(new_nums))]
    del nums[len(new_nums):]
    return len(nums)


print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(removeDuplicates([1, 2, 1, 1, 2]))
print(removeDuplicates([-1, 0, 0, 0, 0, 3, 3]))
print(removeDuplicates([1, 1, -3, 5, 5, 7, 7, 7]))
print(removeDuplicates([1, 3, 5, 5, 3, 1]))
