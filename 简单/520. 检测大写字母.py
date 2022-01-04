# 我们定义，在以下情况时，单词的大写用法是正确的：
# 全部字母都是大写，比如 "USA" 。
# 单词中所有字母都不是大写，比如 "leetcode" 。
# 如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
# 给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。

# 示例 1：
# 输入：word = "USA"
# 输出：true

# 示例 2：
# 输入：word = "FlaG"
# 输出：false


# s.isalnum() #所有字符都是数字或者字母
# s.isalpha() #所有字符都是字母
# s.isdigit() #所有字符都是数字
# s.islower() #所有字符都是小写
# s.isupper() #所有字符都是大写
# s.istitle() #所有单词都是首字母大写，像标题
# s.isspace() #所有字符都是空白字符、\t、\n
# s.upper() #把所有字符中的小写字母转换成大写字母
# s.lower() #把所有字符中的大写字母转换成小写字母
# s.capitalize() #把第一个字母转化为大写字母，其余小写
# s.title() #把每个单词的第一个字母转化为大写，其余小写 
# ord(s)：获得字符 s 的 ASCII 值
# chr(s)：获得数字 s 对应的字母


def detectCapitalUse(word):
  return word.isupper() or word.islower() or word.istitle()  


print(detectCapitalUse("USA"))
print(detectCapitalUse("FlaG"))
