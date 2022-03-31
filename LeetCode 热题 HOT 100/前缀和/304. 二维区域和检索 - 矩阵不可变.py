# 给定一个二维矩阵 matrix，以下类型的多个请求：
# 计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。
# 实现 NumMatrix 类：

# NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
# int sumRegion(int row1, int col1, int row2, int col2) 返回 左上角 (row1, col1) 、右下角 (row2, col2) 所描述的子矩阵的元素 总和 。

# 示例 1：
# 输入: 
# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
# [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
# 输出: 
# [null, 8, 11, 12]
# 解释:
# NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)


class NumMatrix:  
    def __init__(self, matrix):
      self.matrix = matrix
      self.curMatrix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
      for i in range(len(self.matrix)):
        for j in range(len(self.matrix[i])):
          self.curMatrix[i + 1][j + 1] = self.curMatrix[i][j + 1] + self.curMatrix[i + 1][j] - \
            self.curMatrix[i][j] + self.matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
      return self.curMatrix[row2 + 1][col2 + 1] - self.curMatrix[row1][col2 + 1] - \
        self.curMatrix[row2 + 1][col1] + self.curMatrix[row1][col1]
