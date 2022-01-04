# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

#  

# 示例 1：
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"

# 示例 2：
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# 示例 3：
# 输入：s = "A", numRows = 1
# 输出："A"


def convert(s, numRows):
  if numRows == 1:
    return s
  res = ""
  # 初始化一个numRows行len(s)/2列的数组
  temp = [[0 for _ in range(len(s)//2 + 1)] for _ in range(numRows)]
  i = 0
  j = 0
  flag = 1
  for index in range(len(s)):
    temp[i][j] = s[index] 
    if flag == 1:
      i += 1
      if i == numRows - 1:
        flag = -1 * flag
    else:
      i -= 1
      j += 1
      if i == 0:
        flag = -1 * flag
     
  for i in range(len(temp)):
    for j in range(len(temp[i])):
      if temp[i][j] != 0:
        res += temp[i][j]
  return res


# print(convert("PAYPALISHIRING", 3))
# print(convert("PAYPALISHIRING", 4))
# print(convert("A", 1))
print(convert("AB", 1))
