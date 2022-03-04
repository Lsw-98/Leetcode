# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

# 给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，
# 并按上述情形进行了一次旋转。请返回旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为1。  

# 示例 1：
# 输入：[3,4,5,1,2]
# 输出：1

# 示例 2：
# 输入：[2,2,2,0,1]
# 输出：0


def minArray(numbers):
  if len(numbers) == 0:
    return 
  if len(numbers) == 1:
    return numbers[0]
  left = 0
  right = len(numbers) - 1
  index = -1

  while left <= right:
    if numbers[left] > numbers[left + 1]:
      index = left + 1
      numbers = numbers[index:] + numbers[:index]
      break
    elif numbers[right] < numbers[right - 1]:
      index = right
      numbers = numbers[index:] + numbers[:index]
      break
    left += 1
    right -= 1
  
  return numbers[0]
      


print(minArray([3, 4, 5, 1, 2]))
print(minArray([2, 2, 2, 0, 1]))
print(minArray([1, 3, 5]))