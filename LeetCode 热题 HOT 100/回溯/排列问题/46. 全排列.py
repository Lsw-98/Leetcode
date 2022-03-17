# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# 示例 2：
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]

# 示例 3：
# 输入：nums = [1]
# 输出：[[1]]


def permute(nums):
  res = list()
  temp = list()
  
  def backtracking():
    if len(temp) == len(nums):
      res.append(temp[:])
      return 

    for i in range(0, len(nums)):
      if nums[i] in temp:
        continue
      temp.append(nums[i])
      backtracking()
      temp.pop()

  backtracking()
  return res


print(permute([1, 2, 3]))
print(permute([0, 1]))
print(permute([1]))
