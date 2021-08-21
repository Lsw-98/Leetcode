"""

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false

"""


def isPalindrome(s):
    # import re
    # lst = re.findall(r'[a-z0-9]+', s, re.I)
    # new_s = ''.join(lst).lower()
    # print(new_s)
    # return new_s == new_s[::-1]:

    s = list(filter(str.isalnum, s))
    new_s = ''.join(s).lower()
    return new_s == new_s[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome("OP"))
print(isPalindrome("O0"))
