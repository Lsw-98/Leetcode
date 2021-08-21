"""

统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

限制：
0 <= 数组长度 <= 50000

"""

# 基本思路
# 本题要求统计数字 target 的出现次数，
# 可转化为：使用二分法分别找到 左边界 low 和 右边界 high ，易得数字 target 的数量为 high - low - 1


def search(nums, target):
    def helper(tar):
        low, high = 0, len(nums) - 1
        while low <= high:
            m = (low + high) // 2
            if nums[m] <= tar:
                low = m + 1
            else:
                high = m - 1
        return low
    return helper(target) - helper(target - 1)


print(search([5, 7, 7, 8, 8, 10], 8))
print(search([5, 7, 7, 8, 8, 10], 6))
