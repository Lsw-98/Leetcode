// 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
// 分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 - 1 )

// 示例 1：
// 输入：
// ["CQueue", "appendTail", "deleteHead", "deleteHead"]
// [[], [3], [], []]
// 输出：[null, null, 3, -1]

// 示例 2：
// 输入：
// ["CQueue", "deleteHead", "appendTail", "appendTail", "deleteHead", "deleteHead"]
// [[], [], [5], [2], [], []]
// 输出：[null, -1, null, null, 5, 2]


var CQueue = function () {
  this.inStack = []
  this.outStack = []
};

/** 
 * @param {number} value
 * @return {void}
 */
CQueue.prototype.appendTail = function (value) {
  this.inStack.push(value)
};

/**
 * @return {number}
 */
CQueue.prototype.deleteHead = function () {
  const inSize = this.inStack.length
  if (this.inStack.length > 0) {
    for (let i = 0; i < inSize; i++) {
      const temp = this.inStack.pop()
      this.outStack.push(temp)
    }
    const res = this.outStack.pop()
    const outSize = this.outStack.length
    for (let i = 0; i < outSize; i++) {
      const temp = this.outStack.pop()
      this.inStack.push(temp)
    }
    return res
  }
  return -1
};

/**
 * Your CQueue object will be instantiated and called as such:
 * var obj = new CQueue()
 * obj.appendTail(value)
 * var param_2 = obj.deleteHead()
 */
