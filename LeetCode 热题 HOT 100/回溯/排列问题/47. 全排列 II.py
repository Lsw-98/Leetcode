# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 

# 示例 1：
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
 
# 示例 2：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


from matplotlib.style import use


def permuteUnique(nums):
  res = list()
  temp = list()
  used = [0 for _ in range(len(nums))]
  nums.sort()
  
  def backtracking():
    if len(temp) == len(nums):
      res.append(temp[:])
      return 

    for i in range(0, len(nums)):
      if used[i] == 1:
        continue
      if i >= 1 and nums[i] == nums[i - 1] and used[i] == used[i - 1]:
        continue
      temp.append(nums[i])
      used[i] = 1
      backtracking()
      used[i] = 0
      temp.pop()

  backtracking()
  return res


print(permuteUnique([1, 1, 2]))
print(permuteUnique([1, 2, 3]))
