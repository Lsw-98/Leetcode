# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。

# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]

# 示例 2：
# 输入：nums = []
# 输出：[]

# 示例 3：
# 输入：nums = [0]
# 输出：[]


def threeSum(nums):
  res = list()
  nums.sort()
  n = len(nums)

  for i in range(n - 2):
    if i > 0 and nums[i - 1] == nums[i]:
      continue
    if nums[i] + sum(nums[i + 1:i + 3]) > 0:
      continue
    if nums[i] + sum(nums[-1:-3:-1]) < 0:
      continue

    left = i + 1
    right = n - 1
    while left < right:
      if nums[i] + nums[left] + nums[right] == 0:
        res.append([nums[i], nums[left], nums[right]])
        while left < right and nums[left] == nums[left + 1]:
          left += 1
        while left < right and nums[right] == nums[right - 1]:
          right -= 1
        left += 1
        right -= 1
      elif nums[i] + nums[left] + nums[right] > 0:
        right -= 1
      else:
        left += 1
  return res


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([]))
print(threeSum([0]))
