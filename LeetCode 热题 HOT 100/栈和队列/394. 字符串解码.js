/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function (s) {
  const num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  const num_statck = []
  const letter_stack = []
  let left = 0
  let res = ""

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "]" && num_statck.length !== 0 && letter_stack.length !== 0) {
      left -= 1
      num_statck.pop()
      const temp1 = []
      const temp2 = []
      for (let j = letter_stack.length - 1; j >= 0; j--) {
        if (letter_stack[j] !== -1) {
          const t = letter_stack.pop()
          temp2.unshift(t)
        } else {
          letter_stack.pop()
          break
        }
      }

      for (let b = num_statck.length - 1; b >= 0; b--) {
        if (num_statck[b] !== -1) {
          const o = num_statck.pop()
          temp1.unshift(o)
        } else {
          break
        }
      }
      const u = parseInt(temp1.join(""))
      const r = temp2.join("")

      if (left !== 0) {
        let mid = []
        for (let k = 0; k < u; k++) {
          mid += r
        }
        if (letter_stack[letter_stack.length - 1] !== -1) {
          let temp = letter_stack.pop()
          temp += mid
          letter_stack.push(temp)
        } else {
          letter_stack.push(mid)
        }
      } else {
        for (let j = 0; j < u; j++) {
          res += r
        }
      }
    }
    else if (s[i] in num) {
      num_statck.push(s[i])
    } else if (s[i] === "[") {
      left += 1
      letter_stack.push(-1)
      num_statck.push(-1)
    } else {
      if (num_statck.length === 0) {
        res += s[i]
      } else {
        letter_stack.push(s[i])
      }
    }
  }
  return res
};

console.log(decodeString("3[a10[bc]]"))
console.log(decodeString("100[leetcode]"))
