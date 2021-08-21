"""

给你一个整数数组nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集不能包含重复的子集。你可以按 任意顺序 返回解集。


示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

"""


# 子集问题，使用回溯
# 子集不可以有重复数字
def subsets(nums):
    ans = [[]]
    temp = []
    nums.sort()
    n = len(nums)
    used = [0 for _ in range(n)]

    def backtrace(index):
        for i in range(index, n):
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == 0:
                continue
            used[i] = 1
            temp.append(nums[i])
            ans.append(temp[:])
            backtrace(i + 1)
            temp.pop()
            used[i] = 0

    backtrace(0)
    return ans
    

print(subsets([4, 4, 4, 1, 4]))
print(subsets([1, 2, 2]))
print(subsets([1, 2, 3]))
print(subsets([0]))

# ans = [[]]
# if len(nums) == 0:
#     return ans
# temp = []
# used = [0 for _ in range(len(nums))]
# nums.sort()
#
#
# def backtrace(index):
#     for i in range(index, len(nums)):
#         if i - 1 >= 0 and nums[i] == nums[i - 1] and used[i - 1] == 0:
#             continue
#         temp.append(nums[i])
#         ans.append(temp[:])
#         used[i] = 1
#         backtrace(i + 1)
#         used[i] = 0
#         temp.pop()
#
#
# backtrace(0)
# return ans