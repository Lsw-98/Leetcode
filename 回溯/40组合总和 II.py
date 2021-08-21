"""

给定一个数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。

示例1:
输入: candidates =[10,1,2,7,6,1,5], target =8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例2:
输入: candidates =[2,5,2,1,2], target =5,
所求解集为:
[
 [1,2,2],
 [5]
]

"""


# 此题重点在去重
def combinationSum2(candidates, target):
    ans = []
    if len(candidates) == 0 or target == 0:
        return ans
    temp = []
    candidates.sort()
    # used列表用来去重
    used = [0 for _ in range(len(candidates))]
    
    def backtrace(num, index):
        if num > target:
            return
        
        if num == target:
            ans.append(temp[:])
            return

        for i in range(index, len(candidates)):
            if i - 1 >= 0 and candidates[i] == candidates[i - 1] and used[i - 1] == 0:
                continue
            num += candidates[i]
            temp.append(candidates[i])
            used[i] = 1
            backtrace(num, i + 1)
            used[i] = 0
            temp.pop()
            num -= candidates[i]
        
    backtrace(0, 0)
    return ans


print(combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27))
print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(combinationSum2([2, 5, 2, 1, 2], 5))
