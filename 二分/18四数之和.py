"""

给定一个包含n 个整数的数组nums和一个目标值target，判断nums中是否存在四个元素 a，b，c和 d，使得a + b + c + d的值与target相等？
找出所有满足条件且不重复的四元组。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [], target = 0
输出：[]

"""


def fourSum(nums, target):
    nums.sort()
    ans = []
    res = []
    if len(nums) < 4:
        return ans
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            low = j + 1
            high = len(nums) - 1
            while low < high:
                temp = nums[i] + nums[j] + nums[low] + nums[high]
                if temp > target:
                    high -= 1
                elif temp < target:
                    low += 1
                else:
                    ans.append([nums[i], nums[j], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
    ans.sort()
    for x in ans:
        if x not in res:
            res.append(x)
    return res


print(fourSum([2, 2, 2, 2], 8))
print(fourSum([-2, -1, -1, 1, 1, 2, 2], 0))
print(fourSum([1, 0, -1, 0, -2, 2], 0))
print(fourSum([], 0))

# res = []
# ans = []
# n = len(nums)
# if n < 4:
#     return ans
# else:
#     nums.sort()
#     for i in range(n - 3):
#         for j in range(i + 1, n - 2):
#             low = j + 1
#             high = n - 1
#             while low < high:
#                 add = nums[i] + nums[j] + nums[high] + nums[low]
#                 if add < target:
#                     low += 1
#                 elif add > target:
#                     high -= 1
#                 else:
#                     res.append([nums[i], nums[j], nums[high], nums[low]])
#                     # 去重
#                     while low < high and nums[low] == nums[low + 1]:
#                         low += 1
#                     while low < high and nums[high] == nums[high - 1]:
#                         high -= 1
#                     low += 1
#                     high -= 1
# res.sort()
# for i in range(len(res)):
#     if res[i] not in ans:
#         ans.append(res[i])
# return ans
