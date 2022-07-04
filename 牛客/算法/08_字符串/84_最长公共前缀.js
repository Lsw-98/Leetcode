/**
  * 
  * @param strs string字符串一维数组 
  * @return string字符串
  */
function longestCommonPrefix(strs) {
  let res = ""
  for (let i = 0; i < strs.length; i++) {
    let temp = strs[0][i]
    if (temp === undefined) {
      continue
    }
    for (let j = 0; j < strs.length; j++) {
      if (temp !== strs[j][i]) {
        return res
      }
    }
    res += temp
  }
  return res
}
module.exports = {
  longestCommonPrefix: longestCommonPrefix
};

console.log(longestCommonPrefix([]));