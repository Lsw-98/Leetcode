# 如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 没有出现 ，那么这个单词就是 不常见的 。
# 给你两个 句子 s1 和 s2 ，返回所有 不常用单词 的列表。返回列表中单词可以按 任意顺序 组织。

# 示例 1：
# 输入：s1 = "this apple is sweet", s2 = "this apple is sour"
# 输出：["sweet","sour"]

# 示例 2：
# 输入：s1 = "apple apple", s2 = "banana"
# 输出：["banana"]


def uncommonFromSentences(s1, s2):
  s1 = s1.split()
  s2 = s2.split()
  temp = dict()
  res = list()
  for i in s2:
    if i not in temp:
      temp[i] = 1
    else:
      temp[i] += 1
  for j in s1:
    if j not in temp:
      temp[j] = 1
    else:
      temp[j] += 1
  for k in temp:
    if temp[k] == 1:
      res.append(k)
  return res


print(uncommonFromSentences("this apple is sweet", "this apple is sour"))
print(uncommonFromSentences("apple apple", "banana"))
