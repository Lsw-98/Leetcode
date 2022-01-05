"""

罗马数字包含以下七种字符:I，V，X，L，C，D和M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给定一个罗马数字，将其转换成整数。输入确保在 1到 3999 的范围内。

示例1:
输入: num = 3
输出: "III"

示例2:
输入: num = 4
输出: "IV"

示例3:
输入: num = 9
输出: "IX"

示例4:
输入: num = 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.

示例5:
输入: num = 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.

"""


def romanToInt(num):
    # 我的弱智解法--
    # res = ''
    # while num > 0:
    #     if num // 1000 != 0:
    #         for _ in range(num // 1000):
    #             res += 'M'
    #         num = num - 1000 * (num // 1000)
        
    #     if num // 100 != 0:
    #         if num // 100 == 9:
    #             res += 'CM'
    #             num = num - 100 * (num // 100)
    #         elif num // 500 != 0:
    #             res += 'D'
    #             num = num - 500 * (num // 500)
    #         elif num // 100 == 4:
    #             res += 'CD'
    #             num = num - 100 * (num // 100)
    #         if num // 100:
    #             for _ in range(num // 100):
    #                 res += 'C'
    #             num = num - 100 * (num // 100)
    #     if num // 10 != 0:
    #         if num // 10 == 9:
    #             res += 'XC'
    #             num = num - 10 * (num // 10)
    #         elif num // 50 != 0:
    #             res += 'L'
    #             num = num - 50 * (num // 50)
    #         elif num // 10 == 4:
    #             res += 'XL'
    #             num = num - 10 * (num // 10)
    #         if num // 10:
    #             for _ in range(num // 10):
    #                 res += 'X'
    #             num = num - 10 * (num // 10)
    #     if num == 9:
    #         res += 'IX'
    #         num = 0
    #     elif num // 5 != 0:
    #         res += 'V'
    #         num = num - 5 * (num // 5)
    #     elif num == 4:
    #         res += 'IV'
    #         num = 0
    #     if num > 0:
    #         num -= 1
    #         res += 'I'
    # return res

    # 大佬解法
    list1=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    list2=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    result=""
    for i in range(len(list1)):
        while num>=list1[i]:
            result+=list2[i]
            num-=list1[i]
    return result


print(romanToInt(3))
print(romanToInt(4))
print(romanToInt(9))
print(romanToInt(58))
print(romanToInt(1994))
print(romanToInt(2500))
print(romanToInt(2501))
print(romanToInt(60))