function InversePairs(data) {
  const modNum = 1000000007
  let res = 0
  let left = 0
  let right = data.length - 1

  while (left < right) {
    if (data[left] > data[right]) {
      res += 1
      left += 1
    } else {
      right -= 1
    }
  }

  return res % modNum
}
module.exports = {
  InversePairs: InversePairs
};

console.log(InversePairs([1, 2, 3, 4, 5, 6, 7, 0]));
console.log(InversePairs([1, 3, 2, 4, 5, 6, 7]));
