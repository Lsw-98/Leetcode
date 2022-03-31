# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

# 示例 1:
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。

# 示例 2:
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。


def findMaxLength(nums):
  if len(nums) <= 1:
    return 0
  maxLength = 0
  sumNums = 0
  # hashmap的key为求和结果，value为上次的位置
  hashmap = {0: -1}
  for i in range(len(nums)):
    if nums[i] == 0:
      sumNums += 1
    else:
      sumNums -= 1
    if hashmap.get(sumNums) is not None:
      maxLength = max(maxLength, i - hashmap.get(sumNums))
    else:
      hashmap[sumNums] = i
  return maxLength


print(findMaxLength([0, 1]))
print(findMaxLength([0, 1, 0]))
