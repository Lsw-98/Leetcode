"""

给定一个整数数组和一个整数k，判断数组中是否存在两个不同的索引i和j，使得nums [i] = nums [j]，并且 i 和 j的差的 绝对值 至多为 k。

示例1:
输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false

"""


def containsNearbyDuplicate(nums, k):
    # 超时
    # if len(nums) <= 1:
    #     return False
    # else:
    #     for i in range(len(nums) - 1):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] == nums[j] and abs(i - j) <= k:
    #                 print(nums[i], nums[j], abs(i - j))
    #                 return True
    #     return False

    # 建立一个大小不超过k的散列表或者说窗口
    k_windows = set()
    for i in range(len(nums)):
        # 如果当前元素在窗口中存在了，说明满足条件了，直接返回true
        if nums[i] in k_windows:
            return True
        # 否则将该元素添加到窗口中
        k_windows.add(nums[i])
        # 检查窗口的大小是否超过了k，如果超过了k,意味着1.当前窗口一个重复元素都没有，
        # 因为如果有的话，肯定就返回true了

        # 2.当前窗口的第一个元素也就是nums[i-k]没有用了，
        # 因为找不到它的在以k为大小的窗口内的重复元素，所以可以把它删除了。
        if len(k_windows) > k:
            k_windows.remove(nums[i - k])
    return False


print(containsNearbyDuplicate([1, 2, 3, 1], 3))
print(containsNearbyDuplicate([1, 0, 1, 1], 1))
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
