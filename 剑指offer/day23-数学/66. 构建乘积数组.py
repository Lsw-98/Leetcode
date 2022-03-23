# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 
# 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

# 示例:

# 输入: [1,2,3,4,5]
# 输出: [120,60,40,30,24]


def constructArr(a):
  res = [1 for _ in range(len(a))]
  temp = 1
  # 先计算下三角每行乘积，再计算上三角每行乘积
  for i in range(1, len(a)):
    res[i] = res[i - 1] * a[i - 1]
  for j in range(len(a) - 2, -1, -1):    
    temp *= a[j + 1]
    res[j] *= temp
  return res

print(constructArr([1, 2, 3, 4, 5]))
