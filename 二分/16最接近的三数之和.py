"""

给定一个包括n 个整数的数组nums和 一个目标值target。找出nums中的三个整数，使得它们的和与target最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)

"""


def threeSumClosest(nums, target):
    min = float('inf')
    nums.sort()
    for i in range(len(nums)):
        low = i + 1
        high = len(nums) - 1
        while low < high:
            temp = nums[i] + nums[low] + nums[high]
            if temp == target:
                return temp
            if abs(temp - target) < abs(min - target):
                min = temp
            if temp > target:
                high -= 1
            else:
                low += 1
    return min


print(threeSumClosest([-1, 2, 1, -4], 1))
print(threeSumClosest([1, 1, 1, 0], -100))  # 2
print(threeSumClosest([1, 1, -1, -1, 3], -1))  # -1
print(threeSumClosest([0, 0, 0], 1))   # 0
print(threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82))
