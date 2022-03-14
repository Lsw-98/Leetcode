# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
#   1. 只使用数字1到9
#   2. 每个数字 最多使用一次 
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

# 示例 1:
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 解释:
# 1 + 2 + 4 = 7
# 没有其他符合的组合了。

# 示例 2:
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 解释:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# 没有其他符合的组合了

# 示例 3:
# 输入: k = 4, n = 1
# 输出: []
# 解释: 不存在有效的组合。
# 在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。


def combinationSum3(k, n):
  res = list()
  temp = list()
  
  def backtracking(startIndex, count):
    if len(temp) > k:
      return 

    if len(temp) == k and count == n:
      res.append(temp[:])
      return 
    
    for i in range(startIndex, 10):
      temp.append(i)
      count += i
      backtracking(i + 1, count)
      count -= i
      temp.pop()

  backtracking(1, 0)
  return res


print(combinationSum3(9, 45))
print(combinationSum3(3, 9))
print(combinationSum3(4, 1))
