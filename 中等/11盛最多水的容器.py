"""

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在坐标内画 n 条垂直线，
垂直线 i的两个端点分别为(i,ai) 和 (i, 0) 。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。

示例 2：
输入：height = [1,1]
输出：1

示例 3：
输入：height = [4,3,2,1,4]
输出：16

示例 4：
输入：height = [1,2,1]
输出：2

"""


# 超时了，不会优化状态转移方程了
# def maxArea(height):
#     n = len(height)
#     if n <= 1:
#         return 0
#     else:
#         dp = [0 for _ in range(n)]
#         for i in range(n):
#             for j in range(i + 1, n):
#                 dp[j] = max(dp[j], (min(height[i], height[j]) * (j - i)))
#     return dp

# 双指针法
def maxArea(height):
    n = len(height)
    ans = float("-inf")

    if n <= 1:
        return 0
    else:
        low = 0
        high = n - 1
        while low < high:
            ans = max(ans, (high - low) * min(height[high], height[low]))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
    return ans


print(maxArea([2, 3, 4, 5, 18, 17, 6]))
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))
print(maxArea([4, 3, 2, 1, 4]))
print(maxArea([1, 2, 1]))
