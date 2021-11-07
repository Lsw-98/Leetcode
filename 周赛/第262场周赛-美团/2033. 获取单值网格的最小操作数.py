# 给你一个大小为 m x n 的二维整数网格 grid 和一个整数 x 。每一次操作，你可以对 grid 中的任一元素 加 x 或 减 x 。
# 单值网格 是全部元素都相等的网格。
# 返回使网格化为单值网格所需的 最小 操作数。如果不能，返回 -1 。

# 示例 1：
# 输入：grid = [[2,4],[6,8]], x = 2
# 输出：4
# 解释：可以执行下述操作使所有元素都等于 4 ： 
# - 2 加 x 一次。
# - 6 减 x 一次。
# - 8 减 x 两次。
# 共计 4 次操作。

# 示例 2：
# 输入：grid = [[1,5],[2,3]], x = 1
# 输出：5
# 解释：可以使所有元素都等于 3 。

# 示例 3：
# 输入：grid = [[1,2],[3,4]], x = 2
# 输出：-1
# 解释：无法使所有元素相等。


def minOperations(grid, x):
  # 取中位数
  count = 0
  temp = list()
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      temp.append(grid[i][j])
  temp.sort()

  n = len(temp)
  for k in range(n):
    if k == n // 2:
      continue
    temp[k] = temp[n // 2] - temp[k]

  for i in range(len(temp)):
    if i == n // 2:
      continue
    if temp[i] % x != 0:
      return -1
    count += abs(temp[i]) // x
  return count


print(minOperations([[2, 4], [6, 8]], 2))
print(minOperations([[1, 5], [2, 3]], 1))
print(minOperations([[1, 2], [3, 4]], 2))
print(minOperations([[146]], 84))
