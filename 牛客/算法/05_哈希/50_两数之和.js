/**
  * 
  * @param numbers int整型一维数组 
  * @param target int整型 
  * @return int整型一维数组
  */
function twoSum(numbers, target) {
  let obj = {}
  for (let i = 0; i < numbers.length; i++) {
    obj[i] = numbers[i]
  }

  let left = 0
  // let right = map.size - 1
  return obj
  // while (left <= right) {
  //   if (map[left] + numbers[right] < target) {

  //   } else if (numbers[left] + numbers[right] < target) {

  //   } else {
  //     return [left + 1, right + 1]
  //   }
  // }
}

module.exports = {
  twoSum: twoSum
};


console.log(twoSum([3, 2, 4], 6));
console.log(twoSum([0, 4, 3, 0], 0));
