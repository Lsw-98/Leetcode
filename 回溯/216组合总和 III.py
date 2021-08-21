"""

找出所有相加之和为n的k个数的组合。组合中只允许含有 1 -9 的正整数，并且每种组合中不存在重复的数字。

说明：
所有数字都是正整数。
解集不能包含重复的组合。

示例 1:
输入: k = 3, n = 7
输出: [[1,2,4]]

示例 2:
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

"""


def combinationSum3(k, n):
    nums = [i for i in range(1, 10)]
    ans = []
    temp = []

    def backtrace(index, count):
        if count == n and len(temp) == k:
            ans.append(temp[:])

        for i in range(index, len(nums)):
            if count + nums[i] > n:
                break

            count += nums[i]
            temp.append(nums[i])
            backtrace(i + 1, count)
            temp.pop()
            count -= nums[i]

    backtrace(0, 0)
    return ans


print(combinationSum3(2, 18))
print(combinationSum3(9, 45))
print(combinationSum3(3, 7))
print(combinationSum3(3, 9))













# ans = []
#     if k == 0 or n == 0:
#         return ans
#     nums = [i for i in range(1, 10)]
#
#     temp_arr = []
#
#     def backtarce(k, n, start_index, temp):
#         if temp > n:
#             return
#
#         if temp == n and len(temp_arr) == k:
#             ans.append(temp_arr[:])
#             return
#
#         for j in range(start_index, len(nums)):
#             temp += nums[j]
#             temp_arr.append(nums[j])
#             backtarce(k, n, j + 1, temp)
#             temp_arr.pop()
#             temp -= nums[j]
#
#     backtarce(k, n, 0, 0)
#     return ans