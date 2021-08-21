"""

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
如果有多对数字的和等于s，则输出任意一对即可。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

示例 2：
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

限制：

1 <= nums.length <= 10^5
1 <= nums[i]<= 10^6

"""


def twoSum(nums, target):
    # 自己的方法：外层线性查找，内层二分查找
    # 时间复杂度：O(nlogn) 用时988ms
    # for i in range(len(nums)):
    #     temp = target
    #     temp -= nums[i]
    #     low = i + 1
    #     high = len(nums) - 1
    #     while low <= high:
    #         mid = (low + high) // 2
    #         if nums[mid] == temp:
    #             return [nums[i], nums[mid]]
    #         elif nums[mid] > temp:
    #             high = mid - 1
    #         else:
    #             low = mid + 1

    # 题解方法：双指针
    # 时间复杂度：O(n)，用时168ms，效率提高了一点但还是很慢。。。
    low = 0
    high = len(nums) - 1
    while low < high:
        if nums[low] + nums[high] == target:
            return [nums[low], nums[high]]
        elif nums[low] + nums[high] > target:
           high -= 1
        else:
            low += 1


print(twoSum([14, 15, 16, 22, 53, 60], 76))
