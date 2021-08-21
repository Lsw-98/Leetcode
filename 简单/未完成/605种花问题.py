""""

假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组flowerbed 表示花坛，由若干 0 和 1 组成，
其中 0 表示没种植花，1 表示种植了花。另有一个数n ，能否在不打破种植规则的情况下种入n朵花？
能则返回 true ，不能则返回 false。

示例 1：
输入：flowerbed = [1,0,0,0,1], n = 1
输出：true

示例 2：
输入：flowerbed = [1,0,0,0,1], n = 2
输出：false

"""


def canPlaceFlowers(flowerbed, n):
    length = len(flowerbed)
    for i in range(length):
        if i == 0:
            pass
            if flowerbed[i + 1] == flowerbed[i] == 0:
                n -= 1
                flowerbed[i] = 1
        elif i == length - 1 and flowerbed[i] == flowerbed[i - 1] == 0:
            n -= 1
            flowerbed[i] = 1
        elif flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
            n -= 1
            flowerbed[i] = 1
    if n:
        return False
    else:
        return True


# print(canPlaceFlowers([1, 0, 0, 0, 1], 1))
# print(canPlaceFlowers([1, 0, 0, 0, 1], 2))
# print(canPlaceFlowers([0, 0, 1, 0, 1], 1))
print(canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
