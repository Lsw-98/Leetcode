# 给你三个整数数组 nums1、nums2 和 nums3 ，请你构造并返回一个不同数组，且由至少在两个数组中出现的所有值组成。
# 数组中的元素可以按任意顺序排列。

# 示例 1：
# 输入：nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
# 输出：[3,2]
# 解释：至少在两个数组中出现的所有值为：
# - 3 ，在全部三个数组中都出现过。
# - 2 ，在数组 nums1 和 nums2 中出现过。

# 示例 2：
# 输入：nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
# 输出：[2,3,1]
# 解释：至少在两个数组中出现的所有值为：
# - 2 ，在数组 nums2 和 nums3 中出现过。
# - 3 ，在数组 nums1 和 nums2 中出现过。
# - 1 ，在数组 nums1 和 nums3 中出现过。

# 示例 3：
# 输入：nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
# 输出：[]
# 解释：不存在至少在两个数组中出现的值。


def twoOutOfThree(nums1, nums2, nums3):
  res = list()
  for i in nums1:
    if i in nums2 or i in nums3:
     res.append(i)
  for j in nums2: 
    if j in nums3 and j not in nums1:
      res.append(j)
  return list(set(res))


print(twoOutOfThree([1, 1, 3, 2], [2, 3], [3]))
print(twoOutOfThree([3, 1],  [2,3], [1, 2]))
print(twoOutOfThree([1, 2, 2], [4, 3, 3], [5]))
