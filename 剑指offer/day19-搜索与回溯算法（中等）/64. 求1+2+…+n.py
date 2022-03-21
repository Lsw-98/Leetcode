# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

# 示例 1：
# 输入: n = 3
# 输出: 6

# 示例 2：
# 输入: n = 9
# 输出: 45


def sumNums(n):
  num = 1
  def backtrace(count, n):
    if count > n:
      return 0
    return count + backtrace(count + 1, n)

  res = backtrace(num, n)
  return res


print(sumNums(3))
print(sumNums(9))
