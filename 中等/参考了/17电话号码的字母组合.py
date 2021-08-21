"""

给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

"""


def letterCombinations(digits):
    ans = []

    if len(digits) == 0:
        return ans

    digit_word = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    # 递归函数
    def dfs(tmp, index):
        # 递归的终止条件
        # 用index记录每次遍历到字符串的位置，这样性能更好
        if index == len(digits):
            ans.append(tmp)
            return
        # 获取index位置的字符，假设输入的字符是"234"
        # 第一次递归时index为0所以c=2，第二次index为1所以c=3，第三次c=4
        # subString每次都会生成新的字符串，而index则是取当前的一个字符，所以效率更高一点
        c = digits[index]
        # map_string的下表是从0开始一直到9， ord(c)-48 是获取c的ASCII码然后-48,48是0的ASCII
        # 比如c=2时候，2-'0'，获取下标为2,letter_map[2]就是"abc"
        letters = digit_word[ord(c) - 48]

        # 遍历字符串，比如第一次得到的是2，页就是遍历"abc"
        for i in letters:
            # 调用下一层递归，用文字很难描述，请配合动态图理解
            dfs(tmp + i, index + 1)

    dfs("", 0)
    return ans


print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))
