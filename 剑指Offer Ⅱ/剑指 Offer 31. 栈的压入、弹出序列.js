/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function (pushed, popped) {
  const stack = []
  let index = 0
  for (const item of pushed) {
    stack.push(item)
    while (stack.length && stack[stack.length - 1] === popped[index]) {
      stack.pop()
      index += 1
    }
  }
  return stack.length === 0
};

console.log(validateStackSequences([0, 2, 1], [0, 1, 2]));
