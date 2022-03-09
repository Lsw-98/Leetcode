# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

# 示例 2：
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]

# 示例 3：
# 输入：nums = [3,3], target = 6
# 输出：[0,1]


def twoSum(nums, target):
  # 返回一个排序后的nums，第一项是排序前的index，第二项是value
  b = sorted(enumerate(nums), key=lambda i: i[1])
  left = 0
  right = len(nums) - 1
  while left <= right:
    if b[left][1] + b[right][1] > target:
      right -= 1
    elif b[left][1] + b[right][1] < target:
      left += 1
    else:
      return [b[left][0], b[right][0]] 


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
