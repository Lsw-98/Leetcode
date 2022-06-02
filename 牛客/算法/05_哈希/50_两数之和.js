/**
  * 
  * @param numbers int整型一维数组 
  * @param target int整型 
  * @return int整型一维数组
  */
function twoSum(numbers, target) {
  const myMap = new Map()

  for (let i = 0; i < numbers.length; i++) {
    myMap.set(i, numbers[i])
  }

  const arr = Array.from(myMap)
  arr.sort((a, b) => {
    return a[1] - b[1]
  })

  let left = 0
  let right = arr.length - 1

  const res = []

  while (left <= right) {
    if (arr[left][1] + arr[right][1] < target) {
      left += 1
    } else if (arr[left][1] + arr[right][1] > target) {
      right -= 1
    } else {
      res.push(arr[left][0] + 1)
      res.push(arr[right][0] + 1)
      break
    }
  }

  res.sort((a, b) => {
    return a - b
  })

  return res
}

module.exports = {
  twoSum: twoSum
};


console.log(twoSum([3, 2, 4], 6));
console.log(twoSum([5, 75, 25], 100));
