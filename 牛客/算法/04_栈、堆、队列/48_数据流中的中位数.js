let res = ""
// const nums = []

// function Insert(num) {
//   nums.push(num)
// }
function GetMedian(nums) {
  if (nums.length % 2 === 0) {
    res += ((nums[parseInt(nums.length / 2)] + nums[parseInt(nums.length / 2) + 1]) / 2).toFixed(2)

  } else {
    res += nums[parseInt(nums.length / 2) + 1].toFixed(2)
  }
  return res
}
// module.exports = {
//   Insert: Insert,
//   GetMedian: GetMedian
// };

console.log(GetMedian([5, 2, 3, 4, 1, 6, 7, 0, 8]));