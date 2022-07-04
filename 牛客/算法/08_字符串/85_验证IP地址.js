/**
 * 验证IP地址
 * @param IP string字符串 一个IP地址字符串
 * @return string字符串
 */
function solve(IP) {
  let res
  let isV4 = false
  for (let i = 0; i < IP.length; i++) {
    if (IP[i] === ".") {
      res = IP.split(".")
      isV4 = true
      break
    } else if (IP[i] === ":") {
      res = IP.split(":")
      break
    }
  }

  if (isV4) {
    for (let i = 0; i < res.length; i++) {
      if (res[i] > 255 || res[i][0] === "0" || res[i].length === 0) {
        return "Neither"
      }
      for (let j = 0; j < res[i].length; j++) {
        if (/^[A-Za-z]+$/.test(res[i][j])) {
          return "Neither"
        }
      }
    }
    return "IPv4"
  } else {
    for (let i = 0; i < res.length; i++) {
      if (res[i].length === 0 || res[i].length > 4) {
        return "Neither"
      }
      for (let j = 0; j < res[i].length; j++) {
        if (!/^[A-Fa-f0-9]+$/.test(res[i][j])) {
          return "Neither"
        }
      }
    }
    return "IPv6"
  }
}
module.exports = {
  solve: solve
};


console.log(solve("172.016.254.1"));
console.log(solve("20EE:FGb8:85a3:0:0:8A2E:0370:7334"));
console.log(solve("256.256.256.256"));