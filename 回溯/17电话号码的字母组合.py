"""
示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]

"""


def letterCombinations(digits):
    tele = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    ans = []
    temp = []
    n = len(digits)
    if n == 0:
        return ans

    nums = list(map(int, digits))

    def backtrace(index):
        if len(temp) == n:
            ans.append(''.join(temp[:]))
            return

        temp_index = nums[index]
        for i in range(len(tele[temp_index])):
            temp.append(tele[temp_index][i])
            backtrace(index + 1)
            temp.pop()

    backtrace(0)
    return ans


print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))
