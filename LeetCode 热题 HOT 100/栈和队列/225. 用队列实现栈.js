var MyStack = function () {
  this.in_list = []
  this.out_list = []
};

/** 
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function (x) {
  this.in_list.push(x)
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function () {
  const size = this.in_list.length - 1
  for (let i = 0; i < size; i++) {
    const temp = this.in_list.shift()
    this.out_list.push(temp)
  }
  const res = this.in_list.shift()

  for (let i = 0; i < size; i++) {
    const temp = this.out_list.shift()
    this.in_list.push(temp)
  }

  return res
};

/**
 * @return {number}
 */
MyStack.prototype.top = function () {
  const size = this.in_list.length - 1
  for (let i = 0; i < size; i++) {
    const temp = this.in_list.shift()
    this.out_list.push(temp)
  }
  const res = this.in_list.shift()

  for (let i = 0; i < size; i++) {
    const temp = this.out_list.shift()
    this.in_list.push(temp)
  }

  this.in_list.push(res)
  return res
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function () {
  return this.in_list.length === 0 && this.out_list.length === 0
};

