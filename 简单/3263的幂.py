"""

给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3 ** x

示例 1：
输入：n = 27
输出：true

示例 2：
输入：n = 0
输出：false

示例 3：
输入：n = 9
输出：true

示例 4：
输入：n = 45
输出：false
 
提示：
-2 ** 31 <= n <= 2 ** 31 - 1

"""

def isPowerOfThree(n):
    if n <= 0:
        return False
    elif n == 1:
        return True
    else:
        i = 1
        while n > i:
            i *= 3
            if n == i:
                return True
        return False


print(isPowerOfThree(1))
print(isPowerOfThree(27))
print(isPowerOfThree(0))
print(isPowerOfThree(9))
print(isPowerOfThree(45))
