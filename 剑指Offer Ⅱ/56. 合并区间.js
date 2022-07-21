/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  const res = intervals.sort((a, b) => {
    return a[0] - b[0]
  })
  let i = 1
  while (i < res.length) {
    if (res[i - 1][1] < res[i][0]) {
      i += 1
      continue
    } else if (res[i - 1][1] > res[i][0]) {
      if (res[i - 1][1] >= res[i][1]) {
        res.splice(i, 1)
      } else {
        const temp = [res[i - 1][0], res[i][1]]
        res.splice(i - 1, 2)
        res.splice(i - 1, 0, temp)
      }
    } else {
      const temp = [res[i - 1][0], res[i][1]]
      res.splice(i - 1, 2)
      res.splice(i - 1, 0, temp)
    }
  }
  return res
};


console.log(merge([[1, 3], [2, 6], [8, 10], [15, 18]]));
console.log(merge([[1, 4], [4, 5]]));


// 二维数组排序
// intervals.sort((a, b) => a[0] - b[0]);//按照起始位置排序
// const res = [intervals[0]]

// for (let i = 1; i < intervals.length; i++) {
//   if (intervals[i][0] > res[res.length - 1][1]) {
//     res.push(intervals[i])
//     continue
//   }
//   else if (intervals[i][0] <= res[res.length - 1][1] && intervals[i][0] > res[res.length - 1][0]) {
//     if (intervals[i][1] > res[res.length - 1][1]) {
//       const temp = [res[res.length - 1][0], intervals[i][1]]
//       res.pop()
//       res.push(temp)
//     } else {
//       const temp = [res[res.length - 1][0], res[res.length - 1][1]]
//       res.pop()
//       res.push(temp)
//     }
//   } else if (intervals[i][0] <= res[res.length - 1][0]) {
//     if (res[res.length - 1][1] <= intervals[i][1]) {
//       const temp = [intervals[i][0], intervals[i][1]]
//       res.pop()
//       res.push(temp)
//     } else {
//       const temp = [intervals[i][0], res[res.length - 1][1]]
//       res.pop()
//       res.push(temp)
//     }
//   }
// }
// return res