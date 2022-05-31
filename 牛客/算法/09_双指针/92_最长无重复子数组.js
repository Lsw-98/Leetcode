/**
 * 
 * @param arr int整型一维数组 the array
 * @return int整型
 */
function maxLength(arr) {
  let res = []
  let maxLength = 0
  for (let i = 0; i < arr.length; i++) {
    if (res.includes(arr[i])) {
      if (maxLength < res.length) {
        maxLength = res.length
      }
      const tempLength = res.length
      while (res.length > 0) {
        if (res[0] === arr[i]) {
          res.shift()
          break
        }
        res.shift()
      }
    }
    res.push(arr[i])
  }
  if (maxLength < res.length) {
    maxLength = res.length
  }
  return maxLength
}
module.exports = {
  maxLength: maxLength
};


console.log(maxLength("ohvhjdml"));
console.log(maxLength([2, 2, 3, 4, 3]));
console.log(maxLength([1, 2, 3, 4, 1, 5, 6, 7, 8, 1]));
console.log(maxLength([2, 2, 3, 4, 8, 99, 3]));
