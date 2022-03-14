# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用 一次 。
# 注意：解集不能包含重复的组合。 

# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# 示例 2:
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]


def combinationSum2(candidates, target):
  res = list()
  temp = list()
  candidates.sort()

  def backtracking(startIndex, count):
    if count > target:
      return 
    
    if count == target:
      res.append(temp[:])
      return 
    
    for i in range(startIndex, len(candidates)):
      if i > startIndex and candidates[i] == candidates[i - 1]:
        continue
      temp.append(candidates[i])
      count += candidates[i]
      backtracking(i + 1, count)
      count -= candidates[i]
      temp.pop()

  backtracking(0, 0)
  return res


print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(combinationSum2([2, 5, 2, 1, 2], 5))
