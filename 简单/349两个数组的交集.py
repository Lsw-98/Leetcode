"""

给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]

"""


def intersection(nums1, nums2):
    # reslist = []
    # if len(nums1) >= len(nums2):
    #     for i in range(len(nums1)):
    #         if nums1[i] in nums2 and nums1[i] not in reslist:
    #             reslist.append(nums1[i])
    # else:
    #     for i in range(len(nums2)):
    #         if nums2[i] in nums1 and nums2[i] not in reslist:
    #             reslist.append(nums2[i])
    # return reslist
    return list(set(nums1) & set(nums2))


print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
