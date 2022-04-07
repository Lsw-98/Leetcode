/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function (pushed, popped) {
  stack = []
  index = 0
  for (let i of pushed) {
    stack.push(i)
    while (stack.length !== 0 && popped[index] === stack[stack.length - 1]) {
      index += 1
      stack.pop()
    }
  }
  return stack.length === 0
};


console.log(validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]));
console.log(validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]));
console.log(validateStackSequences([1, 0, 2], [2, 1, 0]));
console.log(validateStackSequences([4, 0, 1, 2, 3], [4, 2, 3, 0, 1]));
