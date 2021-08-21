"""

给定一个无重复元素的有序整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，
并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b

示例 1：
输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

示例 2：
输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

示例 3：
输入：nums = []
输出：[]

示例 4：
输入：nums = [-1]
输出：["-1"]

示例 5：
输入：nums = [0]
输出：["0"]

提示：
0 <= nums.length <= 20
-2**31 <= nums[i] <= 2**31 - 1
nums 中的所有值都 互不相同

"""


def summaryRanges(nums):

    # 自己写的垃圾代码  36ms， 14.8MB
    # 设置两指针
    # 写了一个小时，呜呜呜，我可真菜
    # lst = []
    # final_lst = []
    #
    # for i in range(len(nums) - 1):
    #     if nums[i] + 1 != nums[i + 1]:
    #         lst.append(i)
    # n = 1
    # for j in range(len(lst)):
    #     nums.insert(lst[j] + n, ',')
    #     n += 1
    #
    # if len(nums) == 1:
    #     final_lst.append(str(nums[0]))
    # else:
    #     leftInterval = 0
    #     for rightInterval in range(1, len(nums)):
    #         if nums[rightInterval] == ',':
    #             if rightInterval - leftInterval == 1:
    #                 final_lst.append(str(nums[leftInterval]))
    #                 leftInterval = rightInterval + 1
    #             else:
    #                 final_lst.append(str(nums[leftInterval]) + '->' + str(nums[rightInterval - 1]))
    #                 leftInterval = rightInterval + 1
    #         elif leftInterval == len(nums) - 1:
    #             final_lst.append(str(nums[leftInterval]))
    #         elif rightInterval == len(nums) - 1:
    #             final_lst.append(str(nums[leftInterval]) + '->' + str(nums[rightInterval]))
    # return final_lst

    # 别人的代码，效率差不多，耗时一样
    # 但只有9行，我的是28行
    if not nums:
        return []
    res = [[nums[0]]]
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            # 这个-1就很灵性，我怎么都想不到，学习了
            # 添加了尾指针
            res[-1].append(nums[i - 1])
            # 在添加首指针
            res.append([nums[i]])
    # 最后再将nums最后一个元素添加到res
    res[-1].append(nums[-1])
    # f表达式
    return [[f'{a}->{b}', f'{a}'][a == b] for a, b in res]


print(summaryRanges([0, 1, 2, 4, 5, 7]))
print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))
print(summaryRanges([]))
print(summaryRanges([-1]))
print(summaryRanges([0]))
