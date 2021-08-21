"""

给定一个非负整数数组 A，返回一个数组，在该数组中，A 的所有偶数元素之后跟着所有奇数元素。

你可以返回满足此条件的任何数组作为答案。

示例：
输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。

提示：
1 <= A.length <= 5000
0 <= A[i] <= 5000

"""


def sortArrayByParity(A):
    # # 效率有点差，1956ms，优化一下
    # for i in range(len(A)):
    #     if A[i] % 2 != 0:
    #         for j in range(i, len(A)):
    #             if A[j] % 2 == 0:
    #                 A[i], A[j] = A[j], A[i]
    #                 break
    # return A

    # 88ms
    # A.sort(key=lambda x: x % 2)
    # return A

    # 两遍扫描
    # 80ms???????
    lst = []
    for i in range(len(A)):
        if A[i] % 2 == 0:
            lst.append(A[i])
    for j in range(len(A)):
        if A[j] % 2 != 0:
            lst.append(A[j])
    return lst


print(sortArrayByParity([3, 1, 2, 4]))
