function GetLeastNumbers_Solution(input, k) {
  if (k === 0 || input.length === 0) {
    return []
  }

  input.sort(function (a, b) {
    return a - b
  })

  return input.slice(0, k)
}
module.exports = {
  GetLeastNumbers_Solution: GetLeastNumbers_Solution
};


console.log(GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 4));