"""

给定一个 没有重复 数字的序列，返回其所有可能的全排列。

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""


def permute(nums):
    ans = []
    temp = []
    n = len(nums)
    used = [0 for _ in range(n)]
    nums.sort()

    def backtrace():
        if len(temp) == n:
            ans.append(temp[:])
            return

        for i in range(len(nums)):
            if used[i] == 1:
                continue
            # 去重
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == 1:
                continue
            temp.append(nums[i])
            used[i] = 1
            backtrace()
            used[i] = 0
            temp.pop()

    backtrace()
    return ans


print(permute([1, 1, 2]))
print(permute([1, 2, 3]))
