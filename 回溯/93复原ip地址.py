"""

给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。

示例 1：
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]

示例 2：
输入：s = "0000"
输出：["0.0.0.0"]

示例 3：
输入：s = "1111"
输出：["1.1.1.1"]

示例 4：
输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]

示例 5：
输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

"""


def restoreIpAddresses(s):
    SEG_COUNT = 4
    ans = list()
    segments = [0] * SEG_COUNT
    n = len(s)

    def dfs(segId, segStart):
        # 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案
        if segId == SEG_COUNT:
            if segStart == n:
                ipAddr = ".".join(str(seg) for seg in segments)
                ans.append(ipAddr)
            return

        # 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯
        if segStart == n:
            return

        # 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0
        if s[segStart] == "0":
            segments[segId] = 0
            dfs(segId + 1, segStart + 1)

        # 一般情况，枚举每一种可能性并递归
        addr = 0
        for segEnd in range(segStart, n):
            addr = addr * 10 + (ord(s[segEnd]) - ord("0"))
            if 0 < addr <= 0xFF:
                segments[segId] = addr
                dfs(segId + 1, segEnd + 1)
            else:
                break

    dfs(0, 0)
    return ans

    # l=len(s)
    # if l>12 or l<4: return []
    # arr=[]
    # for i in range(1,min(4,l-2)):
    #     for j in range(i+1,min(i+4,l-1)):
    #         for k in range(j+1,min(j+4,l)):
    #             if l-k>3: continue
    #             n=[s[:i],s[i:j],s[j:k],s[k:]]
    #             flag=False
    #             for c in n:
    #                 if c[0]=='0' and c!='0':
    #                     flag=True
    #                     break
    #             if flag: continue
    #             # print(n)
    #             a,b,c,d=map(int,n)
    #             if 0<=a<=255 and 0<=b<=255 and 0<=c<=255 and 0<=d<=255:
    #                 arr.append(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))
    # return arr


print(restoreIpAddresses("25525511135"))
print(restoreIpAddresses("0000"))
print(restoreIpAddresses("1111"))
print(restoreIpAddresses("010010"))
print(restoreIpAddresses("101023"))
