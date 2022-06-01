const stack = []

function push(node) {
  stack.push(node)
}
function pop() {
  if (stack.length > 0) {
    stack.pop()
  }
}
function top() {
  return stack[stack.length - 1]
}
function min() {
  return Math.min(...stack)
}
module.exports = {
  push: push,
  pop: pop,
  top: top,
  min: min
};