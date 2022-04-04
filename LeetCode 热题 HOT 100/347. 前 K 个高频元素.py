# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

# 示例 1:
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]

# 示例 2:
# 输入: nums = [1], k = 1
# 输出: [1]


def topKFrequent(nums, k):
  dit = {}
  for i in nums:
    if i not in dit:
      dit[i] = 1
    else:
      dit[i] += 1
  temp = sorted(dit.items(), key = lambda kv:(kv[1], kv[0]))
  res = []
  for j in range(k):
    res.append(temp[len(temp) - j - 1][0])
  return res


print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))
