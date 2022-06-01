/**
  * 
  * @param s string字符串 
  * @return bool布尔型
  */
function isValid(s) {
  const stack = []
  const left = ["(", "{", "["]

  for (let i = 0; i < s.length; i++) {
    if (left.includes(s[i])) {
      stack.push(s[i])
    } else {
      if (stack.length > 0) {
        const temp = stack.pop()
        if ((temp === "(" && s[i] === ")") || (temp === "{" && s[i] === "}") || (temp === "[" && s[i] === "]")) {
          continue
        } else {
          return false
        }
      } else {
        return false
      }
    }
  }
  if (stack.length > 0) {
    return false
  }
  return true
}
module.exports = {
  isValid: isValid
};