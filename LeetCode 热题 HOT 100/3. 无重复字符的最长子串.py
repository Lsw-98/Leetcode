# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

# 示例 2:
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

# 示例 3:
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


from collections import deque


def lengthOfLongestSubstring(s):
  if s == "":
    return 0
  length = len(s)
  if length == 1:
    return 1
  dp = [0 for _ in range(length)]
  dp[0] = 1
  temp = deque()
  temp.append(s[0])
  numIndex = 0
  
  for i in range(1, length):
    if s[i] not in temp:
      temp.append(s[i])
      dp[i] = dp[i - 1] + 1
    else:
      numIndex = temp.index(s[i])
      for _ in range(numIndex + 1):
        temp.popleft()
      temp.append(s[i])
      dp[i] = len(temp)
  return max(dp)


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("dvdf"))
