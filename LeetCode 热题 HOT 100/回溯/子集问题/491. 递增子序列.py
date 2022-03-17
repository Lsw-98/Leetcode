# 给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
# 数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。

# 示例 1：
# 输入：nums = [4,6,7,7]
# 输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

# 示例 2：
# 输入：nums = [4,4,3,2,1]
# 输出：[[4,4]]


def findSubsequences(nums):
  # 5s
  # res = list()
  # temp = list()
  # used = [0 for _ in range(len(nums))]
  
  # def backtracking(index):
  #   if len(temp) >= 2 and temp not in res:
  #     res.append(temp[:])

  #   for i in range(index, len(nums)):
  #     if i > 0 and nums[i] == nums[i - 1] and used[i] == used[i - 1]:
  #       continue
  #     if len(temp) >= 1 and nums[i] < temp[-1]:
  #       continue
  #     temp.append(nums[i])
  #     used[i] = 1
  #     backtracking(i + 1)
  #     used[i] = 0
  #     temp.pop()
    
  # backtracking(0)
  # return res

  # 80ms
  res = list()
  temp = list()
  def backtracking(index):
    if len(nums) >= 2:
      if temp[-1] >= temp[-2]:
        res.append(temp[:])
      else:
        return 
    
    for i in range(index, len(nums)):
      if nums[i] in nums[index:i]:continue
      temp.append(nums[i])
      backtracking(i + 1)
      temp.pop()

  backtracking(0)
  return res

print(findSubsequences([4, 6, 7, 7]))
print(findSubsequences([4, 4, 3, 2, 1]))
