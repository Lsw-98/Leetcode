"""

给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例1：
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]

示例2：
输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10]重叠。

"""


def insert(intervals, newInterval):
    intervals.append(newInterval)
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


print(insert([[1, 3], [6, 9]], [2, 5]))
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
