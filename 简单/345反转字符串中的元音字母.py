"""

编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1：
输入："hello"
输出："holle"

示例 2：
输入："leetcode"
输出："leotcede"

"""


def reverseVowels(s):
    low = 0
    high = len(s) - 1
    s = list(s)
    vowels = "aeiouAEIOU"
    while low < high:
        if s[low] not in vowels:
            low += 1
        elif s[high] not in vowels:
            high -= 1
        else:
            temp = s[low]
            s[low] = s[high]
            s[high] = temp
            low += 1
            high -= 1
    return ''.join(s)


print(reverseVowels("hello"))
print(reverseVowels("leetcode"))
print(reverseVowels("aA"))
