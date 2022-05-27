/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 比较版本号
 * @param version1 string字符串 
 * @param version2 string字符串 
 * @return int整型
 */
function compare(version1, version2) {
  const v1 = version1.split('.')
  const v2 = version2.split('.')
  const vInt1 = v1.map((item) => {
    return parseInt(item)
  })
  const vInt2 = v2.map((item) => {
    return parseInt(item)
  })

  if (vInt1.length < vInt2.length) {
    for (let i = 0; i < vInt2.length - vInt1.length; i++) {
      vInt1.push(0)
    }
  } else if (vInt1.length > vInt2.length) {
    for (let i = 0; i <= vInt1.length - vInt2.length; i++) {
      vInt2.push(0)
    }
  }

  for (let i = 0; i < vInt1.length; i++) {
    if (vInt1[i] < vInt2[i]) {
      return -1
    } else if (vInt1[i] > vInt2[i]) {
      return 1
    }
  }
  return 0
}
module.exports = {
  compare: compare
};


console.log(compare("1.1", "1.1.1"));
console.log(compare("0.226", "0.36"));
console.log(compare("1.0.1", "1"));
