# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

# 示例 1:
# 输入：s = "abaccdeff"
# 输出：'b'

# 示例 2:
# 输入：s = "" 
# 输出：' '


def firstUniqChar(s):
  if s == "":
    return ' '
  dic = dict()
  for i in s:
    if i not in dic:
      dic[i] = 1
    else:
      dic[i] += 1
  for key,value in dic.items():
    if value == 1:
      return key
  return " "


print(firstUniqChar("abaccdeff"))
print(firstUniqChar("loveleetcode"))
