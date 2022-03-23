# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

# 示例 1:
# 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2


def majorityElement(nums):
  dic = dict()
  for i in nums:
    if i not in dic:
      dic[i] = 1 
    else:
      dic[i] += 1
  for k,v in dic.items():
    if v >= len(nums) // 2:
      return k


print(majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
