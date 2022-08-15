/**
 * @param {string} str
 * @return {number}
 */
var strToInt = function (str) {
  const res = [];
  let flag = true;
  let isFirst = true;
  const nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
  for (let i = 0; i < str.length; i++) {
    if (str[i] === " " || str[i] === "+") {
      continue
    } else if (isFirst && str[i] !== "-" && !nums.includes(str[i])) {
      return 0
    } else {
      isFirst = false
    }

    if (str[i] === ".") {
      const temp = parseInt(res.join(""))
      return temp
    }

    if (str[i] === "-" && res.length && flag) {
      continue
    }
    if (str[i] === "-" && res.length === 0 && flag) {
      flag = false
      res.push(str[i])
    } else if (nums.includes(str[i])) {
      res.push(str[i])
    }
  }

  if (res.length) {
    const temp = parseInt(res.join(""))
    if (isNaN(temp)) {
      return 0
    }
    if (temp > (Math.pow(2, 31) - 1)) {
      return 2147483648
    }
    if (temp < -(Math.pow(2, 31))) {
      return -2147483648
    }
    return temp
  } else {
    return 0
  }
};

console.log(strToInt("42"));
console.log(strToInt("   -42"));
console.log(strToInt("4193 with words"));
console.log(strToInt("words and 987"));
console.log(strToInt("-91283472332"));
console.log(strToInt("3.1415926"));