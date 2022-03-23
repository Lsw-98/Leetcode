# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

# 示例 1：
# 输入：target = 9
# 输出：[[2,3,4],[4,5]]

# 示例 2：
# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]


def findContinuousSequence(target):
  # 回溯，超时。也有可能是我的回溯时间复杂度太高了。。。
  # res = list()
  # temp = list()
  # nums = [i + 1 for i in range(target)]
  # def backtrace(index, countNum):
  #   if countNum == target:
  #     tempLst = [i for i in range(temp[0], temp[0] + len(temp))]
  #     if tempLst == temp:
  #       res.append(temp[:])
  #     return

  #   for i in range(index, len(nums) // 2 + 1):
  #     countNum += nums[i]
  #     temp.append(nums[i])
  #     backtrace(i + 1, countNum)
  #     temp.pop()
  #     countNum -= nums[i]

  # backtrace(0, 0)
  # return res

  # 滑动窗口
  res = list()
  nums = [i + 1 for i in range(target)]
  for i in range(2, len(nums) // 2):
    pass


print(findContinuousSequence(9))
print(findContinuousSequence(15))
