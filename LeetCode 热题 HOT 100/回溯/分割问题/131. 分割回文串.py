# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 回文串 是正着读和反着读都一样的字符串。

# 示例 1：
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]

# 示例 2：
# 输入：s = "a"
# 输出：[["a"]]


def partition(s):
  res= list()
  path = list()

  def backtracking(index):
    if index >= len(s):
      res.append(path[:])
      return 
    
    for i in range(index, len(s)):
      temp = s[index:i + 1]
      if temp == temp[::-1]:
        path.append(temp)
        backtracking(i + 1)
        path.pop()
  
  backtracking(0)
  return res

print(partition("aab"))
print(partition("a"))
