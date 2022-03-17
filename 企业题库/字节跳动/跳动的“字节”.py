# 题目描述
# “字节”在数轴 0 点出发，向左或向右跳动（左右横跳），第一次跳 1 个单位，第二次 2 个单位，
# 以此类推。给定系列目标 [x1, x2, ..., xn]，“字节”依次跳动到给定目标，并在到达后重置跳跃步长，
# 继续按 1, 2,... 步长跳往下一目标。求“字节”跳动到 [x1, x2, ..., xn] 的最小步数 [s1, s2, ..., sn]

# 示例一
# 输入： nums = [2, 1]
# 输出：3, 4
# 解释：
# 从 0 跳动到节点 2 的最小路径是 0 -> 1 -> -1 -> 2，步数为 3
# 从 2 跳动到节点 1 的最短路劲是 2 -> 1，步数为 3 + 1

# 示例二
# 输入： nums = [1, 2, 2]
# 输出：1, 2, 2
# 解释：
# 从 0 跳动到节点 1 的最小路径是 0 -> 1，步数为 1
# 从 1 跳动到节点 2 的最小路径是 1 -> 2，步数为 1 + 1
# 从 1 跳动到节点 2 的最小路径是 2，步数为 2

# 数据范围
# 1<=n<=100
# -10^7 <= xi <= 10^7


lst = list(map(int, input().split()))

def jump_to(gap):
    n = int((2 * gap) ** .5)
    if n*(n + 1) < 2 * gap: # 定位上界
        n += 1
    if gap & 1: # 奇数情形
        if n % 4 in (1, 2): return n
        return n + (1 if n % 4 == 0 else 2)
    if n % 4 in (0, 3): return n
    return n + (1 if (n % 4) == 2 else 2)

def min_jump(nums):
    gaps = [abs(nums[i+1] - nums[i]) for i in range(len(nums)-1)]
    gaps.insert(0, abs(nums[0]))
    totalstep, res = 0, []
    for gap in gaps:
        totalstep += jump_to(gap)
        res.append(totalstep)
    return res

print(min_jump(lst))
