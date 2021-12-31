"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:
输入:n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""


def combine(n, k):
  res = []
  path = []
  
  def backtrace(n, k, StartIndex):
    if len(path) == k:
      res.append(path[:])
      return 

    for i in range(StartIndex, n + 1):
      path.append(i)
      backtrace(n, k, i + 1)
      path.pop()
  backtrace(n, k, 1)
  return res


print(combine(4, 2))
print(combine(4, 1))

# res = list()
# nums = [i + 1 for i in range(n)]

# return res


#     ans = []
#     if n == 0 or k == 0:
#         return ans
#     nums = [i for i in range(1, n + 1)]
#
#     # def backtrace(nums_temp, curr_temp, startindex):
#     #     if len(curr_temp) == k:
#     #         ans.append(curr_temp[:])  # 浅拷贝
#     #         return
#     #
#     #     for j in range(startindex, n):
#     #         curr_temp.append(nums[j])
#     #         back(nums[startindex:], curr_temp, j + 1)
#     #         curr_temp.pop()
#     #
#     # backtrace(nums, [], 0)
#     # return ans
#
#     temp = []
#
#     def backtrace(n, k, start_index):
#         if len(temp) == k:
#             ans.append(temp[:])
#             return
#
#         for j in range(start_index, n - (k - len(temp)) + 1):
#             temp.append(nums[j])
#             backtrace(n, k, j + 1)
#             temp.pop()
#
#     backtrace(n, k, 0)
#     return ans

# ans = []
#     temp = []

#     def backtrace(index):
#         if len(temp) == k:
#             ans.append(temp[:])

#         for i in range(index, n + 1):
#             if len(temp) < k:
#                 temp.append(i)
#                 backtrace(i + 1)
#                 temp.pop()
#     backtrace(1)
#     return ans



