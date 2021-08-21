"""

给你一个长度为n的整数数组，请你判断在 最多 改变1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的：对于数组中所有的i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

示例 1:
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

示例 2:
输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。

"""


def checkPossibility(nums):
    changed = False
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if changed:
                return False
            changed = True
            # 修改num[i]会导致nums[i-1] > nums[i]
            if i > 0 and nums[i - 1] > nums[i + 1]:
                nums[i + 1] = nums[i]
            else:
                nums[i] = nums[i + 1]
    return True


print(checkPossibility([5, 7, 1, 8]))
print(checkPossibility([4, 2, 3]))
print(checkPossibility([4, 2, 1]))
print(checkPossibility([3, 4, 2, 3]))
print(checkPossibility([-1, 4, 2, 3]))
