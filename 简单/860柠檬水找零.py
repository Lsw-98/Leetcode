"""

在柠檬水摊上，每一杯柠檬水的售价为5美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。
你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回true，否则返回 false。

示例 1：
输入：[5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。

示例 2：
输入：[5,5,10]
输出：true

示例 3：
输入：[10,10]
输出：false

示例 4：
输入：[5,5,10,10,20]
输出：false
解释：
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。

"""


# 148ms, 就这垃圾代码都能击败96？
def lemonadeChange(bills):
    denomination = [0 for _ in range(5)]
    if bills[0] > 5:
        return False
    else:
        for i in range(len(bills)):
            if bills[i] == 5:
                denomination[0] += 1
            else:
                if 5 < bills[i] <= 10:
                    if (bills[i] - 5) // 5 > denomination[0]:
                        return False
                    else:
                        denomination[0] -= 1
                        denomination[1] += 1
                elif 10 < bills[i] <= 20:
                    if denomination[1] >= 1:
                        bills[i] -= 10
                        denomination[1] -= 1
                        if (bills[i] - 5) // 5 > denomination[0]:
                            return False
                        else:
                            denomination[0] -= 1
                            denomination[2] += 1
                    elif denomination[0] >= 3:
                        denomination[0] -= 3
                        denomination[2] += 1
                    else:
                        return False
        return True


print(lemonadeChange([5, 5, 5, 5, 20, 20, 5, 5, 20, 5]))
# print(lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20]))
# print(lemonadeChange([5, 5, 5, 10, 20]))
# print(lemonadeChange([5, 5, 10]))
# print(lemonadeChange([10, 10]))
# print(lemonadeChange([5, 5, 10, 10, 20]))
