# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

# 示例 1:
# 输入: [10,2]
# 输出: "102"

# 示例 2:
# 输入: [3,30,34,5,9]
# 输出: "3033459"


def minNumber(nums):
  def mySort(a, b):
    if a + b > b + a:
      return True
    else:
      return False

  nums = list(map(str, nums))
  nums.sort()

  # 冒泡排序
  for i in range(len(nums)):
    for j in range(len(nums) - i - 1):
      if mySort(nums[j], nums[j + 1]):
        nums[j], nums[j + 1] = nums[j + 1], nums[j]
  return nums


print(minNumber([10, 2]))
print(minNumber([3, 30, 34, 5, 9]))
