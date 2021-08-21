"""

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于⌊ n/2 ⌋的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例1:
输入: [3,2,3]
输出: 3

示例2:
输入: [2,2,1,1,1,2,2]
输出: 2

"""


def majorityElement(nums):
    from collections import Counter
    mostele = Counter(nums)
    return list(mostele.keys())[list(mostele.values()).index(max(mostele.values()))]


print(majorityElement([3, 2, 3]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
