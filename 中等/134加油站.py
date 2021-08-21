"""

在一条环路上有N个加油站，其中第i个加油站有汽油gas[i]升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1个加油站需要消耗汽油cost[i]升。
你从其中的一个加油站出发，开始时油箱为空。
如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明:
如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。

示例1:
输入:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
输出: 3

解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。

示例 2:
输入:
gas  = [2,3,4]
cost = [3,4,3]
输出: -1

解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。

"""


# 5132ms,超时了啊,呜呜呜
# def canCompleteCircuit(gas, cost):
# if sum(gas) < sum(cost):
#     return -1
# else:
#     # 开始出发的索引
#     start = 0
#     for i in range(len(gas)):
#         total = 0
#         if gas[i] - cost[i] >= 0:
#             start = i
#             for j in range(start, len(gas) + start):
#                 if j >= len(gas) - 1:
#                     total += gas[j - len(gas)] - cost[j - len(gas)]
#                 else:
#                     total += gas[j] - cost[j]
#                 if total < 0:
#                     break
#                 if j - len(gas) + 1 == start:
#                     return start
#     return -1


# 别人的,44ms
def canCompleteCircuit(gas, cost):
    # total记录可获得的总油量-总油耗， cur记录当前油耗情况， ans记录出发位置
    total, cur, ans = 0, 0, 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        cur += gas[i] - cost[i]
        if cur < 0:                     # 油不够开到i站
            cur = 0                     # cur置零，在新位置重新开始计算油耗情况
            ans = i + 1                 # 将起始位置改成i+1
    return ans if total >= 0 else -1    # 如果获得的汽油的量小于总油耗，则无法回到起点


print(canCompleteCircuit([5, 8, 2, 8], [6, 5, 6, 6]))
print(canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]))
print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(canCompleteCircuit([2, 3, 4], [3, 4, 3]))
print(canCompleteCircuit([4, 5, 2, 6, 5, 3], [3, 2, 7, 3, 2, 9]))
