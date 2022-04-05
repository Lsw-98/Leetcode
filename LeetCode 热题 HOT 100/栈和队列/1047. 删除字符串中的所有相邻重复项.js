/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function (s) {
  const stack = []
  for (let i of s) {
    if (stack.length > 0) {
      if (stack[stack.length - 1] === i) {
        stack.pop()
      } else {
        stack.push(i)
      }
    } else {
      stack.push(i)
    }
  }
  return stack.join('')
};


console.log(removeDuplicates("abbaca"));