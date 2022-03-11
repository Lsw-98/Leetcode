# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。

# 示例 1：
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# 示例 2：
# 输入：n = 1, k = 1
# 输出：[[1]]


def combine(n, k):
  res = list()   # 结果链表
  nums = list()  # 中间链表，用于存储长度为k的组合

  # 定义回溯方法
  def backtracking(n, k, startIndex):
    if len(nums) == k:
      res.append(nums[:])
      return 

    # 从1到n依次遍历  
    for i in range(startIndex, n + 1):
      nums.append(i)
      # 因为是组合，所以每次传入startIndex后面的数字即可
      backtracking(n, k, i + 1)
      nums.pop()
  
  backtracking(n, k, 1)
  return res


print(combine(4, 2))
print(combine(1, 1))
