const in_stack = []
const out_stack = []

function push(node) {
  in_stack.push(node)
}
function pop() {
  if (in_stack.length > 0) {
    const inSize = in_stack.length
    for (let i = 0; i < inSize; i++) {
      const temp = in_stack.pop()
      out_stack.push(temp)
    }
    const res = out_stack.pop()
    const outSize = out_stack.length
    for (let i = 0; i < outSize; i++) {
      const temp = out_stack.pop()
      in_stack.push(temp)
    }
    return res
  }
}
module.exports = {
  push: push,
  pop: pop
};