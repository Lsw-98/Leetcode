/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 * 
 * @param str string字符串 待判断的字符串
 * @return bool布尔型
 */
function judge(str) {
  if (str.length === 0 || str.length === 1) {
    return true
  }

  let left = 0
  let right = str.length - 1

  while (left <= right) {
    if (str[left] !== str[right]) {
      return false
    }
    left += 1
    right -= 1
  }

  return true
}
module.exports = {
  judge: judge
};


console.log(judge("aba"));
console.log(judge("ranko"));
console.log(judge("yamatomaya"));
console.log(judge("a"));