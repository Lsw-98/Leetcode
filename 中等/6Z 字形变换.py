"""

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行Z 字形排列。

比如输入字符串为 "PAYPALISHIRING"行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

示例 3：
输入：s = "A", numRows = 1
输出："A"

"""


def convert(s, numRows):
    s_temp = list(s)
    list_num_rows = []
    for i in range(numRows):
        list_num_rows.append([])
    count = -1
    flag = True
    for j in range(len(s_temp)):
        if count:
            count += 1
            list_num_rows[count].append(s_temp[j])
            count += 1

        else:
            count -= 1
            list_num_rows[count].append(s_temp[j])
            count -= 1

    for _ in range(numRows):
        print(s[_])
    return 0


print(convert("PAYPALISHIRING", 3))
# print(convert("PAYPALISHIRING", 4))
# print(convert("A", 1))
