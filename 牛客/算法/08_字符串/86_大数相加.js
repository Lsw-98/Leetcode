/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 * 计算两个数之和
 * @param s string字符串 表示第一个整数
 * @param t string字符串 表示第二个整数
 * @return string字符串
 */
function solve(s, t) {
  if (s === "") {
    return t
  } else if (t === "") {
    return s
  }

  let res = ""
  let temp = 0

  s = s.split("")
  t = t.split("")

  while (s.length || t.length || temp) {
    temp += ~~s.pop() + ~~t.pop()
    res = (temp % 10) + res
    temp = temp > 9
  }

  return res
}
module.exports = {
  solve: solve
};

console.log(solve("0", "0"));