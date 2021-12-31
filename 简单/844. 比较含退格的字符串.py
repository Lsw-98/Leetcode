# 给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，请你判断二者是否相等。# 代表退格字符。
# 如果相等，返回 true ；否则，返回 false 。
# 注意：如果对空文本输入退格字符，文本继续为空。

# 示例 1:
# 输入：s = "ab#c", t = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。

# 示例 2：
# 输入：s = "ab##", t = "c#d#"
# 输出：true
# 解释：s 和 t 都会变成 “”。

# 示例 3：
# 输入：s = "a##c", t = "#a#c"
# 输出：true
# 解释：s 和 t 都会变成 “c”。

# 示例 4：
# 输入：s = "a#c", t = "b"
# 输出：false
# 解释：s 会变成 “c”，但 t 仍然是 “b”。


def backspaceCompare(s, t):
  ls = list(s)
  lt = list(t)
  for i in range(len(s)):
    if s[i] == '#':
      ls[i] = 0
      for j in range(i - 1, -1, -1):
        if ls[j] != 0:
          ls[j] = 0
          break

  for p in range(len(t)):
    if t[p] == '#':
      lt[p] = 0
      for q in range(p - 1, -1, -1):
        if lt[q] != 0:
          lt[q] = 0
          break
  
  for i in range(len(ls) - 1, -1, -1):
    if ls[i] == 0:
      ls.remove(0)

  for p in range(len(lt) - 1, -1, -1):
    if lt[p] == 0:
      lt.remove(0)
    
  return ls == lt

  
print(backspaceCompare("xywrrmp", "xywrrm#p"))