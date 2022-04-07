var MaxQueue = function () {
  this.queue = []
};

/**
 * @return {number}
 */
MaxQueue.prototype.max_value = function () {
  if (this.queue.length === 0) {
    return Math.max.apply(null, this.queue)
  }
  return -1
};

/** 
 * @param {number} value
 * @return {void}
 */
MaxQueue.prototype.push_back = function (value) {
  this.queue.push(value)
};

/**
 * @return {number}
 */
MaxQueue.prototype.pop_front = function () {
  if (this.queue.length === 0) {
    return this.queue.shift()
  }
  return -1
};
