# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

# 返回 滑动窗口中的最大值。


# 示例 1：
# 输入：nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# 输出：[3, 3, 5, 5, 6, 7]
# 解释：
# 滑动窗口的位置                最大值
# --------------- -----
# [1  3 - 1] - 3  5  3  6  7       3
# 1 [3 - 1 - 3] 5  3  6  7       3
# 1  3 [-1 - 3  5] 3  6  7       5
# 1  3 - 1 [-3  5  3] 6  7       5
# 1  3 - 1 - 3 [5  3  6] 7       6
# 1  3 - 1 - 3  5 [3  6  7]      7

# 示例 2：
# 输入：nums = [1], k = 1
# 输出：[1]


from collections import deque


def maxSlidingWindow(nums, k):
    # 超时  52/61
    # res = []
    # for i in range(len(nums) - k + 1):
    #     res.append(max(nums[i:k+i]))
    # return res

    # 超时  59/61
    # queue = deque()
    # res = []
    # for i in range(k):
    #     queue.append(nums[i])
    # maxNum = max(queue)
    # res.append(maxNum)
    # for j in range(k, len(nums)):
    #     temp = queue.popleft()
    #     queue.append(nums[j])
    #     if temp != maxNum and queue[-1] < maxNum:
    #         res.append(maxNum)
    #     else:
    #         maxNum = max(queue)
    #         res.append(maxNum)
    # return res

    if k == 1:
        return nums
    n = len(nums)
    q = deque()
    for i in range(k):
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
    res = [nums[q[0]]]
    for i in range(k, n):
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
        while q[0] <= i-k:
            q.popleft()
        res.append(nums[q[0]])
    return res


print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(maxSlidingWindow([1], 1))
