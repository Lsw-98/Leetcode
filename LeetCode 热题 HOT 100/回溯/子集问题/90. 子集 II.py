# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

# 示例 1：
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]


from matplotlib.style import use


def subsetsWithDup(nums):
  res = list()
  temp = list()
  nums.sort()
  used = [0 for _ in range(len(nums))]

  def backtracking(index):   
    res.append(temp[:]) 

    for i in range(index, len(nums)):
      if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == used[i]:
        continue
      temp.append(nums[i])           
      used[i] = 1
      backtracking(i + 1)
      used[i] = 0
      temp.pop()

  backtracking(0)
  return res

print(subsetsWithDup([1, 2, 2]))
print(subsetsWithDup([0]))
