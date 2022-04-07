/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
  const c = ["+", "-", "*", "/"]
  const res = []
  for (let i of tokens) {
    if (c.includes(i)) {
      if (i === "+") {
        temp1 = res.pop()
        temp2 = res.pop()
        res.push(temp1 + temp2)
      } else if (i === "-") {
        temp1 = res.pop()
        temp2 = res.pop()
        res.push(temp2 - temp1)
      } else if (i === "*") {
        temp1 = res.pop()
        temp2 = res.pop()
        res.push(temp1 * temp2)
      } else {
        let count = 0
        temp1 = res.pop()
        temp2 = res.pop()
        if (temp1 < 0) {
          temp1 *= -1
          count += 1
        }
        if (temp2 < 0) {
          temp2 *= -1
          count += 1
        }
        if (count === 1) {
          temp = Math.floor(temp2 / temp1)
          temp *= -1
          res.push(temp)
        } else {
          res.push(Math.floor(temp2 / temp1))
        }
      }
    } else {
      res.push(parseInt(i))
    }
  }
  return res[0]
};

console.log(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]));