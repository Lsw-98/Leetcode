"""

给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

示例 1：
输入：["bella","label","roller"]
输出：["e","l","l"]

示例 2：
输入：["cool","lock","cook"]
输出：["c","o"]

提示：
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母

"""


def commonChars(A):
    lst = []
    for i in A[0]:
        count1 = A[1].count(i)
        count2 = A[2].count(i)
        if count1 <= 0 or count2 <= 0:
            continue
        else:
            lst.append(i)
            count1 -= 1
            count2 -= 1
    return lst


print(commonChars(["bella", "label", "roller"]))
print(commonChars(["cool", "lock", "cook"]))