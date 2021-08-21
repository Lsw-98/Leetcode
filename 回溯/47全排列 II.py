"""

给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""


def permuteUnique(nums):
    ans = []
    temp = []
    used = [0 for _ in range(len(nums))]
    nums.sort()

    def backtrace():
        if len(temp) == len(nums):
            ans.append(temp[:])
            return

        for i in range(len(nums)):
            if used[i] == 1:
                continue
            if i - 1 >= 0 and nums[i] == nums[i - 1] and used[i - 1] == 1:
                continue
            temp.append(nums[i])
            used[i] = 1
            backtrace()
            used[i] = 0
            temp.pop()

    backtrace()
    return ans


print(permuteUnique([1, 1, 2]))
print(permuteUnique([1, 2, 3]))
