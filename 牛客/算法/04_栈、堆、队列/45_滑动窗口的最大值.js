function maxInWindows(num, size) {
  const res = []
  const temp = []
  for (let i = 0; i < size; i++) {
    temp.push(num[i])
  }

  for (let i = size; i < num.length; i++) {
    res.push(Math.max(...temp))
    temp.shift()
    temp.push(num[i])
  }
  res.push(Math.max(...temp))
  return res
}
module.exports = {
  maxInWindows: maxInWindows
};

console.log(maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3));