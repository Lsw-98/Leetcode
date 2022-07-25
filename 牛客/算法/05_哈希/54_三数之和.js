/**
 * 
 * @param num int整型一维数组 
 * @return int整型二维数组
 */
function threeSum(num) {
  const res = []
  if (num.length < 3) return res
  num.sort((a, b) => { return a - b })

  for (let i = 0; i < num.length; i++) {
    if (i > 0 && num[i] === num[i - 1]) {
      continue
    }
    let left = i + 1
    let right = num.length - 1
    while (left < right) {
      if (left > i + 1 && num[left] === num[left - 1]) {
        left += 1
        continue
      }
      if (num[i] + num[left] + num[right] === 0) {
        res.push([num[i], num[left], num[right]])
        left += 1
        right -= 1
      } else if (num[i] + num[left] + num[right] < 0) {
        left += 1
      } else {
        right -= 1
      }
    }
  }

  return res
}
module.exports = {
  threeSum: threeSum
};

console.log(threeSum([-2, 0, 0, 2, 2]));