# 0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
# 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。


# 示例 1：
# 输入: n = 5, m = 3
# 输出: 3

# 示例 2：
# 输入: n = 10, m = 17
# 输出: 2


def lastRemaining(n, m):
  # 约瑟夫环，超时
  # if n == 1 or n == 0:
  #   return n
  # nums = [_ for _ in range(n)]
  # temp = 0
  # while len(nums) > 1:
  #   temp = (temp + m - 1) % len(nums)
  #   del nums[temp]
  # return nums[0]

  x = 0
  # 直接过滤了n=0和n=1的情况
  for i in range(2, n + 1):
      x = (x + m) % i
  return x


print(lastRemaining(5, 3))
print(lastRemaining(10, 17))
