# 统计一个数字在排序数组中出现的次数。

# 示例 1:
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2

# 示例 2:
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0


def search(nums, target):
  # 顺序查找
  # res = 0
  # for i in nums:
  #   if target == i:
  #     res += 1
  # return res 

  # 二分查找
  left = 0
  right = len(nums) - 1
  res = 0
  while left <= right:
      if nums[left] == target:
          res += 1
          left += 1
      elif nums[right] == target:
          res += 1
          right -= 1
      else:
          left += 1
          right -= 1
  return res


print(search([5, 7, 7, 8, 8, 10], 8))
print(search([5, 7, 7, 8, 8, 10], 6))
