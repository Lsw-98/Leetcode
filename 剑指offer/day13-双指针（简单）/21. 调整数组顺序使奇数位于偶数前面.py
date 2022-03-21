# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

# 示例：
# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4] 
# 注：[3,1,2,4] 也是正确的答案之一。


def exchange(nums):
  # left = 0
  # right = len(nums) - 1
  # res = list()
  # while left < right:
  #   if nums[left] % 2 == 0:
  #     res.append(nums[left])
  #   else:
  #     res.insert(0, nums[left])  
  #   if nums[right] % 2 == 0:
  #     res.append(nums[right])
  #   else:
  #     res.insert(0, nums[right])  
  #   left += 1
  #   right -= 1
  # if left == right:
  #   if nums[left] % 2 == 0:
  #     res.append(nums[left])
  #   else:
  #     res.insert(0, nums[left])  
  # return res

  mid = nums[len(nums) // 2]
  left, right = [], []
  nums.remove(mid)
  for i in nums:
    if i % 2 == 0:
      right.append(i)
    else:
      left.append(i)
  return left + [mid] + right



print(exchange([1, 2, 3, 4]))
print(exchange([1, 3, 5]))
