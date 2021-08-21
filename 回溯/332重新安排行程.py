"""

给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序
所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始

提示：
如果存在多种有效的行程，请你按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）
假定所有机票至少存在一种合理的行程。
所有的机票必须都用一次 且 只能用一次

示例 1：
输入：[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出：["JFK", "MUC", "LHR", "SFO", "SJC"]

示例 2：
输入：[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
解释：另一种有效的行程是["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后

"""


def findItinerary(tickets):
    # Hierholzer 算法
    # import collections
    # import heapq
    #
    # stack = list()
    # vec = collections.defaultdict(list)
    # for depart, arrive in tickets:
    #     vec[depart].append(arrive)
    # # print(vec)
    # for key in vec:
    #     # 使用堆的优先级排序
    #     heapq.heapify(vec[key])
    # # print(vec)
    #
    # def dfs(curr):
    #     while vec[curr]:
    #         tmp = heapq.heappop(vec[curr])
    #         dfs(tmp)
    #     stack.append(curr)
    #
    # dfs("JFK")
    # return stack[::-1]

    from collections import defaultdict
    ticket_dict = defaultdict(list)
    for item in tickets:
        ticket_dict[item[0]].append(item[1])
        ticket_dict[item[0]].sort()
    # print(ticket_dict)
    path = ['JFK']

    def backtrack(cur_from):
        if len(path) == len(tickets) + 1:  # 结束条件
            return True
        for _ in ticket_dict[cur_from]:
            cur_to = ticket_dict[cur_from].pop(0)  # 删除当前节点
            path.append(cur_to)  # 做选择
            if backtrack(cur_to):  # 进入下一层决策树
                return True
            path.pop()  # 取消选择
            ticket_dict[cur_from].append(cur_to)  # 恢复当前节点
        return False

    backtrack('JFK')
    return path


# print(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
