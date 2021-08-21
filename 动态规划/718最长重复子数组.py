"""

给两个整数数组A和B，返回两个数组中公共的、长度最长的子数组的长度。

示例
输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1]

"""

"""

  B   3   2   1   4   7
A 0   0   0   0   0   0
1 0   0   0   1   0   0

2 0   0   1   0   0   0
 
3 0   1   0   0   0   0

2 0   0   1   0   0   0

1 0   0   0   1   0   0

"""


def findLength(A, B):
    # 3160ms，动态规划超时,gg. 动态规划 not yyds
    # dp = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
    # ans = float('-inf')
    # for i in range(1, len(A) + 1):
    #     for j in range(1, len(B) + 1):
    #         if A[i - 1] == B[j - 1]:
    #             dp[i][j] = dp[i - 1][j - 1] + 1
    #     res = max(res, max(dp[i]))
    # return ans

    # 滑动窗口
    # 2912ms
    # def maxLength(addA, addB, length):
    #     ret = k = 0
    #     for i in range(length):
    #         if A[addA + i] == B[addB + i]:
    #             k += 1
    #             ret = max(ret, k)
    #         else:
    #             k = 0
    #     return ret
    #
    # n, m = len(A), len(B)
    # ret = 0
    # for i in range(n):
    #     length = min(m, n - i)
    #     ret = max(ret, maxLength(i, 0, length))
    # for i in range(m):
    #     length = min(n, m - i)
    #     ret = max(ret, maxLength(0, i, length))
    # return ret

    # 哈希 + 二分
    # 100ms
    base, mod = 113, 10 ** 9 + 9

    def check(length: int) -> bool:
        hashA = 0
        for i in range(length):
            hashA = (hashA * base + A[i]) % mod
        bucketA = {hashA}
        mult = pow(base, length - 1, mod)
        for i in range(length, len(A)):
            hashA = ((hashA - A[i - length] * mult) * base + A[i]) % mod
            bucketA.add(hashA)

        hashB = 0
        for i in range(length):
            hashB = (hashB * base + B[i]) % mod
        if hashB in bucketA:
            return True
        for i in range(length, len(B)):
            hashB = ((hashB - B[i - length] * mult) * base + B[i]) % mod
            if hashB in bucketA:
                return True

        return False

    left, right = 0, min(len(A), len(B))
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans


print(findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
print(findLength([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]))
