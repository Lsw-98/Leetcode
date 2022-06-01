/**
 * 
 * @param num int整型一维数组 
 * @return int整型二维数组
 */
function permute(num) {
  const res = []
  const temp = []
  const used = new Array(num.length).fill(0)

  function backtrace() {
    if (temp.length === num.length) {
      res.push(JSON.parse(JSON.stringify(temp)))
      return
    }

    for (let i = 0; i < num.length; i++) {
      if (used[i] === 1) {
        continue
      }

      temp.push(num[i])
      used[i] = 1
      backtrace()
      used[i] = 0
      temp.pop()
    }
  }

  backtrace()
  return res
}
module.exports = {
  permute: permute
};
