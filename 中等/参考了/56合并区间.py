"""

给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例2:
输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

提示：
intervals[i][0] <= intervals[i][1]

"""


# 基本思路
# 我们用数组 merged 存储最终的答案。
# 首先，我们将列表中的区间按照左端点升序排序。
# 然后我们将第一个区间加入 merged 数组中，并按顺序依次考虑之后的每个区间：
# 如果当前区间的左端点在数组 merged 中最后一个区间的右端点之后，那么它们不会重合，
# 我们可以直接将这个区间加入数组 merged 的末尾；
# 否则，它们重合，我们需要用当前区间的右端点更新数组 merged 中最后一个区间的右端点，将其置为二者的较大值。
def merge(intervals):
    intervals.sort()
    merged = []
    merged.append(intervals[0])
    for i in range(1, len(intervals)):
        if merged[-1][1] < intervals[i][0]:
            merged.append(intervals[i])
        else:
            if merged[-1][1] < intervals[i][1]:
                merged[-1][1] = intervals[i][1]
    return merged


print(merge([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16], [4, 8]]))
