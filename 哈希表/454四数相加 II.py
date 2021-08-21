"""

给定四个包含整数的数组列表A , B , C , D ,计算有多少个元组 (i, j, k, l)，使得A[i] + B[j] + C[k] + D[l] = 0。

A, B, C, D 具有相同的长度N，且 0 ≤ N ≤ 500 。最终结果不会超过2 ** 31 - 1 。

例如:
输入:
A = [1, 2]
B = [-2,-1]
C = [-1, 2]
D = [0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

"""


def fourSumCount(A, B, C, D):
    res = 0
    dic = {}
    for a in A:
        for b in B:
            total1 = a + b
            dic[total1] = dic.get(total1, 0) + 1
    for c in C:
        for d in D:
            total2 = c + d
            if -total2 in dic:
                res += dic[-total2]
    return res


print(fourSumCount([-1, -1], [-1, 1], [-1, 1], [1, -1]))
# print(fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
