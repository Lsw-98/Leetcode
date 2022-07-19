var CQueue = function () {
  this.in_stack = []
  this.out_stack = []
};

/** 
 * @param {number} value
 * @return {void}
 */
CQueue.prototype.appendTail = function (value) {
  this.in_stack.push(value)
};

/**
 * @return {number}
 */
CQueue.prototype.deleteHead = function () {
  if (this.in_stack.length === 0) {
    return -1
  }
  const inSize = this.in_stack.length - 1
  for (let i = 0; i < inSize; i++) {
    this.out_stack.push(this.in_stack.pop())
  }

  const res = this.in_stack.pop()
  const outSize = this.out_stack.length
  for (let i = 0; i < outSize; i++) {
    this.in_stack.push(this.out_stack.pop())
  }
  return res
};

/**
 * Your CQueue object will be instantiated and called as such:
 * var obj = new CQueue()
 * obj.appendTail(value)
 * var param_2 = obj.deleteHead()
 */
