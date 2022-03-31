# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为k的子数组的个数 。

# 示例 1：
# 输入：nums = [1,1,1], k = 2
# 输出：2

# 示例 2：
# 输入：nums = [1,2,3], k = 3
# 输出：2


def subarraySum(nums, k):
  # 前缀和 超时
  # res = 0
  # sumNums = [0]
  # for i in range(len(nums)):
  #   sumNums.append(sumNums[-1] + nums[i])
  # for start in range(len(sumNums) - 1):
  #   for end in range(start + 1, len(sumNums)):
  #     if sumNums[end] - sumNums[start] == k:
  #       res += 1
  # return res

  # 前缀和+哈希表
  res = 0
  # key代表前缀和，value代表和出现的次数
  hashmap = {0 : 1}
  sumNums = 0
  for i in nums:
    sumNums += i
    if (sumNums - k) in hashmap.keys():
      res += hashmap[sumNums - k]
    if sumNums in hashmap.keys():
      hashmap[sumNums] += 1
    else:
      hashmap[sumNums] = 1
  return res


print(subarraySum([1, 1, 1], 2))
print(subarraySum([1, 2, 3], 3))
