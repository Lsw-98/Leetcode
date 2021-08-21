"""

给定一个无重复元素的数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates中的数字可以无限制重复被选取。

说明：
所有数字（包括target）都是正整数。
解集不能包含重复的组合。

示例1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
 [2,2,2,2],
 [2,3,3],
 [3,5]
]

"""


def combinationSum(candidates, target):
    ans = []
    if len(candidates) == 0 or target == 0:
        return ans

    temp = []

    def backtrace(count, index):
        if sum(temp) == target:
            # temp.sort()
            # if temp not in ans:
            ans.append(temp[:])
            return

        for i in range(index, len(candidates)):
            if count + candidates[i] > target:
                continue
            count += candidates[i]
            temp.append(candidates[i])
            backtrace(count, i)
            temp.pop()
            count -= candidates[i]

    backtrace(0, 0)
    return ans


print(combinationSum([1, 2], 4))
print(combinationSum([2, 7, 6, 3, 5, 1], 9))
print(combinationSum([2, 3, 6, 7], 7))
print(combinationSum([2, 3, 5], 8))
