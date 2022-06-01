function Permutation(str) {
  const res = []
  const temp = []
  const used = new Array(str.length).fill(0)

  str = str.split("")
  str.sort()

  function backtrace() {
    if (temp.length === str.length) {
      res.push(JSON.parse(JSON.stringify(temp)).join(""))
      return
    }

    for (let i = 0; i < str.length; i++) {
      if (used[i] === 1) {
        continue
      }

      if (i > 0 && str[i] === str[i - 1] && used[i - 1] === 1) {
        continue
      }

      temp.push(str[i])
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
  Permutation: Permutation
};

console.log(Permutation("aba"));