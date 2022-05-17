function minNumberInRotateArray(rotateArray) {
  let res = 0
  let left = 1
  while (left < rotateArray.length) {
    if (rotateArray[left] < rotateArray[left - 1]) {
      break
    }
    left += 1
  }
  return left >= rotateArray.length ? rotateArray[res] : rotateArray[left]
}
module.exports = {
  minNumberInRotateArray: minNumberInRotateArray
};

console.log(minNumberInRotateArray([1, 2, 2, 2, 2, 2]));