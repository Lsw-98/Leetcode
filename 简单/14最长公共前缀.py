"""

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串""。

示例1:
输入: ["flower","flow","flight"]
输出: "fl"

示例2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母a-z。

"""


def longestcommonprefix(strs):

    # 注意传入的参数是str，不是list
    # 使用max()函数和min()函数求出最大字符串长度和最小字符串
    # max()函数和min()函数的参数为字符串时，比较的是字符的大小
    if strs:
        maxs = max(strs)
        mins = min(strs)
        print(maxs, mins)
        n = len(mins)
        m = 0
        while m < n and mins[m] == maxs[m]:
            m += 1
        return mins[:m]
    else:
        return ""


print(longestcommonprefix(["flower", "flow", "feigh"]))
print(longestcommonprefix(["dog", "racecar", "car"]))
