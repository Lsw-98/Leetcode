# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

# 示例 1：
# 输入：nums = [3,4,3,3]
# 输出：4

# 示例 2：
# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1


def singleNumber(nums):
  nums.sort()
  if nums[0] ^ nums[1]:
    return nums[0]
  if nums[-1] ^ nums[-2]:
    return nums[-1]
  for i in range(1, len(nums) - 1):
    if nums[i] ^ nums[i - 1] and nums[i] ^ nums[i + 1]:
      return nums[i]
  


print(singleNumber([3, 4, 3, 3]))
print(singleNumber([9, 1, 7, 9, 7, 9, 7]))
