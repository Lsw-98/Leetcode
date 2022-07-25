/**
  * 
  * @param numbers int整型一维数组 
  * @param target int整型 
  * @return int整型一维数组
  */
function twoSum(numbers, target) {
  const m = new Map()
  for (let i = 0; i < numbers.length; i++) {
    m.set(i, numbers[i])
  }
  const arr = Array.from(m)
  arr.sort((a, b) => {
    return a[1] - b[1]
  })

  let left = 0
  let right = arr.length - 1
  while (left <= right) {
    if (arr[left][1] + arr[right][1] === target) return arr[left][0] > arr[right][0] ? [arr[right][0] + 1, arr[left][0] + 1] : [arr[left][0] + 1, arr[right][0] + 1]
    else if (arr[left][1] + arr[right][1] < target) left += 1
    else right -= 1
  }
}

module.exports = {
  twoSum: twoSum
};

console.log(twoSum([3, 2, 4], 6));
console.log(twoSum([5, 75, 25], 100));
console.log(twoSum([0, 4, 3, 0], 0));
