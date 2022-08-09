/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 * 计算成功举办活动需要多少名主持人
 * @param n int整型 有n个活动
 * @param startEnd int整型二维数组 startEnd[i][0]用于表示第i个活动的开始时间，startEnd[i][1]表示第i个活动的结束时间
 * @return int整型
 */
function minmumNumberOfHost(n, startEnd) {

  let start = startEnd.map(item => item[0])
  let end = startEnd.map(item => item[1])
  start.sort((a, b) => a - b)
  end.sort((a, b) => a - b)

  let count = 0, endIndex = 0
  for (let i = 0; i < start.length; i++) {
    if (start[i] < end[i]) {
      count++
    } else {
      endIndex++
    }
  }
  return count
}
module.exports = {
  minmumNumberOfHost: minmumNumberOfHost
};

console.log(minmumNumberOfHost(2, [[1, 2], [2, 3]]));
console.log(minmumNumberOfHost(2, [[1, 3], [2, 4]]));
