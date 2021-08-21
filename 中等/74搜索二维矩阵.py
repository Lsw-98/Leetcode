"""

编写一个高效的算法来判断 m * n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

    1. 每行中的整数从左到右按升序排列。
    2. 每行的第一个整数大于前一行的最后一个整数。

示例1:
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

示例2:
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false

"""


# 嗨呀，不要觉得自己做不出中等的题目，多练就行了，加油！！！
# 32ms  94.98%用户
def searchMatrix(matrix, target):
    h = len(matrix)
    if h == 0:
        return False
    m = len(matrix[0])
    if m == 0:
        return False

    temp = 0
    while temp < len(matrix):
        if matrix[temp][0] == target:
            return True
        elif matrix[temp][0] < target:
            temp += 1
        else:
            break
    temp -= 1

    # 这一步还可以用二分实现
    # for i in range(len(matrix[temp])):
    #     if matrix[temp][i] == target:
    #         return True
    # return False

    # 40ms
    # 没懂二分为什么还慢了。。
    low = 0
    high = len(matrix[temp]) - 1
    while low <= high:
        mid = (low + high) // 2
        if matrix[temp][mid] == target:
            return True
        elif matrix[temp][mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False


print(searchMatrix([[]], 0))
print(searchMatrix([[], [], []], 0))
print(searchMatrix([[1]], 2))
print(searchMatrix([[1, 3]], 3))
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
