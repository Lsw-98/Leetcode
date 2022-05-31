/*
 * function Interval(a, b){
 *   this.start = a || 0;
 *   this.end = b || 0;
 * }
 */

/**
 * 
 * @param intervals Interval类一维数组 
 * @return Interval类一维数组
 */
function merge(intervals) {
  if (intervals.length < 2) {
    return intervals
  }
  // 二维数组排序
  intervals.sort((a, b) => a[0] - b[0]);//按照起始位置排序
  let res = [intervals[0]]

  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] > res[res.length - 1][1]) {
      res.push(intervals[i])
      continue
    }
    // else if (intervals[i][0] <= res[res.length - 1][1] && intervals[i][0] > res[res.length - 1][0]) {
    //   if (intervals[i][1] > res[res.length - 1][1]) {
    //     const temp = [res[res.length - 1][0], intervals[i][1]]
    //     res.pop()
    //     res.push(temp)
    //   } else {
    //     const temp = [res[res.length - 1][0], res[res.length - 1][1]]
    //     res.pop()
    //     res.push(temp)
    //   }
    // } else if (intervals[i][0] <= res[res.length - 1][0]) {
    //   if (res[res.length - 1][1] <= intervals[i][1]) {
    //     const temp = [intervals[i][0], intervals[i][1]]
    //     res.pop()
    //     res.push(temp)
    //   } else {
    //     const temp = [intervals[i][0], res[res.length - 1][1]]
    //     res.pop()
    //     res.push(temp)
    //   }
    // }
    else if (res[res.length - 1][1] < intervals[i][1]) {
      res[res.length - 1][1] = intervals[i][1]
    }
  }
  return res
}

module.exports = {
  merge: merge
};


console.log(merge([[10, 30], [20, 60], [80, 100], [150, 180]]));
console.log(merge([[0, 10], [10, 20]]));
console.log(merge([[1, 4], [0, 2]]));
console.log(merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]));
