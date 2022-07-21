/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function (pushed, popped) {
  for (let i = 1; i < popped.length - 1; i++) {
    if (popped[i - 1] > popped[i] && popped[i + 1] > popped[i]) {
      return false
    }
  }
  return true
};