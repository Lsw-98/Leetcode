"""

对于非负整数X而言，X的数组形式是每位数字按从左到右的顺序形成的数组。
例如，如果X = 1231，那么其数组形式为[1,2,3,1]。

给定非负整数 X 的数组形式A，返回整数X+K的数组形式。

示例 1：
输入：A = [1,2,0,0], K = 34
输出：[1,2,3,4]
解释：1200 + 34 = 1234

示例 2：
输入：A = [2,7,4], K = 181
输出：[4,5,5]
解释：274 + 181 = 455

示例 3：
输入：A = [2,1,5], K = 806
输出：[1,0,2,1]
解释：215 + 806 = 1021

示例 4：
输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
输出：[1,0,0,0,0,0,0,0,0,0,0]
解释：9999999999 + 1 = 10000000000

提示：
1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
如果 A.length > 1，那么 A[0] != 0

"""


def addToArrayForm(A, K):
    # 6448ms，效率好慢啊
    # A.reverse()
    # sumA = A[0]
    # for i in range(1, len(A)):
    #     sumA += A[i] * 10 ** i
    # sumA += K
    # res = list(map(int, str(sumA)))
    # return res

    # 360ms
    return list(map(int, str(int(''.join(map(str, A))) + K)))


print(addToArrayForm([1, 2, 0, 0], 34))
print(addToArrayForm([2, 7, 4], 181))
print(addToArrayForm([2, 1, 5], 806))
print(addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1))
