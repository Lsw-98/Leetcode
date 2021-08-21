"""

如果所给格子的颜色是白色，请你返回true，如果是黑色，请返回false。
给定坐标一定代表国际象棋棋盘上一个存在的格子。坐标第一个字符是字母，第二个字符是数字。

示例 1：
输入：coordinates = "a1"
输出：false
解释：如上图棋盘所示，"a1" 坐标的格子是黑色的，所以返回 false

示例 2：
输入：coordinates = "h3"
输出：true
解释：如上图棋盘所示，"h3" 坐标的格子是白色的，所以返回 true

示例 3：
输入：coordinates = "c7"
输出：false

"""


def squareIsWhite(coordinates):
    coordinates = list(coordinates)
    if coordinates[0] in ('a', 'c', 'e', 'g'):
        if int(coordinates[1]) % 2 == 0:
            return True
        else:
            return False
    else:
        if int(coordinates[1]) % 2 == 0:
            return False
        else:
            return True


print(squareIsWhite('a1'))
print(squareIsWhite('h3'))
print(squareIsWhite('c7'))
