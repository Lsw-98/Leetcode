# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

# 示例 1：
# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]

# 示例 2：
# 输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]


def singleNumbers(nums):
  res = list()
  nums.sort()
  if nums[0] ^ nums[1]:
    res.append(nums[0])
  if nums[-1] ^ nums[-2]:
    res.append(nums[-1])
  for i in range(1, len(nums) - 1):
    if nums[i] ^ nums[i - 1] and nums[i] ^ nums[i + 1]:
      res.append(nums[i])
  return res


print(singleNumbers([4, 1, 4, 6]))
print(singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]))
