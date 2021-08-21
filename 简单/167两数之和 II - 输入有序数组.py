"""

给定一个已按照 升序排列的整数数组numbers ，请你从数组中找出两个数满足相加之和等于目标数target 。
函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。
numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例 1：
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

示例 2：
输入：numbers = [2,3,4], target = 6
输出：[1,3]

示例 3：
输入：numbers = [-1,0], target = -1
输出：[1,2]

"""


def twoSum(numbers, target):
    # 双指针
    low = 0
    high = len(numbers) - 1
    while low < high:
        if numbers[low] + numbers[high] == target:
            return [low + 1, high + 1]
        elif numbers[low] + numbers[high] > target:
            high -= 1
        else:
            low += 1


# print(twoSum([2, 7, 11, 15, 21], 13))
# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([2, 3, 4], 6))
print(twoSum([-1, 0], -1))
# print(twoSum([0, 0, 3, 4], 0))
