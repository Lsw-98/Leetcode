# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

# 示例 1：
# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]

# 示例 2：
# 输入：arr = [0,1,2,1], k = 1
# 输出：[0]


def getLeastNumbers(arr, k):
  # 冒泡排序，超时
  # for i in range(len(arr)):
  #   for j in range(len(arr) - i -1):
  #     if arr[j] > arr[j + 1]:
  #       arr[j], arr[j + 1] = arr[j + 1], arr[j]
  # return arr[:k]

  # 快排
  def quick_sort(arr):
    if len(arr) < 2:
      return arr
    # 选取基准
    mid = arr[len(arr) // 2]
    # 定义基准两边的列表
    left, right = [], []
    # 从原始数组中移除基准值
    arr.remove(mid)
    # 和基准值进行比较，大的放右边，小的放左边
    for i in arr:
      if i >= mid:
        right.append(i)
      else:
        left.append(i)
    # 迭代比较
    return quick_sort(left) + [mid] + quick_sort(right)
  
  return quick_sort(arr)[0:k]


print(getLeastNumbers([3, 2, 1], 2))
print(getLeastNumbers([0, 1, 2, 1], 1))
