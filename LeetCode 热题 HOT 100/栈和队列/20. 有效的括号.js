/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const left = ["(", "{", "["]
  const stack = []
  for (let i of s) {
    if (left.includes(i)) {
      stack.push(i)
    }
    else {
      if (stack.length !== 0) {
        if (i == ")" && stack[stack.length - 1] == "(") {
          stack.pop()
        }
        else if (i == "}" && stack[stack.length - 1] == "{") {
          stack.pop()
        }
        else if (i == "]" && stack[stack.length - 1] == "[") {
          stack.pop()
        }
        else {
          return false
        }
      }
      else {
        return false
      }
    }
  }
  if (stack.length === 0) {
    return true
  }
  return false
};

console.log(isValid("()"));
console.log(isValid("()[]{}"));
console.log(isValid("(]"));
console.log(isValid("([)]"));
console.log(isValid("{[]}"));