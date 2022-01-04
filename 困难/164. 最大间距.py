# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
# 如果数组元素个数小于 2，则返回 0。

# 示例 1:
# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。

# 示例 2:
# 输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。


def maximumGap(nums):
  if len(nums) < 2:
    return 0
  res = 0
  nums.sort()
  for i in range(1, len(nums)):
    if res < abs(nums[i] - nums[i - 1]):
      res = abs(nums[i] - nums[i - 1])
  return res


print(maximumGap([3, 6, 9, 1]))
print(maximumGap([10]))
