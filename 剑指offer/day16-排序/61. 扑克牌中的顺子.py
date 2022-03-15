# 从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，
# 即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

# 示例 1:
# 输入: [1,2,3,4,5]
# 输出: True

# 示例 2:
# 输入: [0,0,1,2,5]
# 输出: True


def isStraight(nums):
  joker = 0
  temp = list()
  for i in nums:
    if i == 0:
      joker += 1
      continue
    temp.append(i)
  newLst = list(set(temp))
  newLst.sort()
  if newLst[-1] - newLst[0] > 5:
    return False
  elif len(newLst) + joker < 5:
    return False
  else:
    return True
    
      

# print(isStraight([10, 11, 0, 12, 6]))
# print(isStraight([1, 2, 3, 4, 5]))
# print(isStraight([0, 0, 1, 2, 5]))
print(isStraight([1, 6, 5, 4, 2]))
