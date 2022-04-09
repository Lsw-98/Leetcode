# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 

# 示例 1：
# 输入：digits = "23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

# 示例 2：
# 输入：digits = ""
# 输出：[]

# 示例 3：
# 输入：digits = "2"
# 输出：["a", "b", "c"]


def letterCombinations(digits):
    const = [[""], [""], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"],
             ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
    res = list()
    if len(digits) == 0:
        return res
    temp = list()
    nums = list(map(int, digits))

    def backtrace(index):
        if len(temp) == len(nums):
            res.append(''.join(temp[:]))
            return

        for i in range(index, len(digits)):
            for j in range(len(const[nums[i]])):
                temp.append(const[nums[i]][j])
                backtrace(i + 1)
                temp.pop()

    backtrace(0)
    return res


print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))
