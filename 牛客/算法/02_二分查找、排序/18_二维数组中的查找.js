function Find(target, array) {
  let row = 0
  let column = array[0].length - 1

  while (0 <= row && row < array.length && 0 <= column && column < array[0].length) {
    if (array[row][column] > target) {
      column -= 1
    } else if (array[row][column] < target) {
      row += 1
    } else {
      return true
    }
  }
  return false
}
module.exports = {
  Find: Find
};

console.log(Find(5, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]))
