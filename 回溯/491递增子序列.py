"""

给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是 2

示例：
输入：[4, 6, 7, 7]
输出：[[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

"""


def findSubsequences(nums):
    ans = []
    temp = []

    def backtrace(index):
        if len(temp) >= 2:
            if temp[-1] >= temp[-2]:
                ans.append(temp[:])
            else:
                return

        for i in range(index, len(nums)):
            if nums[i] in nums[index:i]:
                continue
            temp.append(nums[i])
            backtrace(i + 1)
            temp.pop()

    backtrace(0)
    return ans


print(findSubsequences([1, 2, 1, 1]))
# print(findSubsequences([4, 6, 7, 7]))
# print(findSubsequences([4, 4, 3, 2, 1]))
# print(len(findSubsequences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1])))
# print(findSubsequences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
