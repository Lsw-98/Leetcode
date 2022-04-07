# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

# 示例 1:
# 输入: nums = [1, 1, 1, 2, 2, 3], k = 2
# 输出: [1, 2]

# 示例 2:
# 输入: nums = [1], k = 1
# 输出: [1]


def topKFrequent(nums, k):
    dic = {}
    res = []
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    dicSort = sorted(dic.items(), key=lambda d: d[1], reverse=True)
    for j in range(k):
        res.append(dicSort[j][0])
    return res


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1], 1))
