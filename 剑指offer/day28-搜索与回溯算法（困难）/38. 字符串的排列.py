# 输入一个字符串，打印出该字符串中字符的所有排列。

# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

# 示例:
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]


def permutation(s):
  s = list(s)
  res = list()
  temp = list()  
  length = len(s)
  used = [0 for _ in range(length)]
  s.sort()

  def backtrace():
    if len(''.join(temp)) == length:
      res.append(''.join(temp[:]))
      return 

    for i in range(length):
      if used[i] == 1:
        continue
      if i >= 1 and s[i] == s[i - 1] and used[i - 1] == 1:
        continue
      temp.append(s[i])
      used[i] = 1
      backtrace()
      used[i] = 0
      temp.pop()

  backtrace()
  return res


print(permutation("abc"))
