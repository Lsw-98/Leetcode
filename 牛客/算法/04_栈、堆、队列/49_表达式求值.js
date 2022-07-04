/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 * 返回表达式的值
 * @param s string字符串 待计算的表达式
 * @return int整型
 */
function solve(s) {
  let nums = [];
  let ops = [];
  let map = new Map()

  map.set('(', -1)
  map.set('+', 1)
  map.set('-', 1)
  map.set('*', 2)

  function calc() {
    let right = nums.pop()
    let left = nums.pop()
    let sign = ops.pop()
    switch (sign) {
      case '+': nums.push(left + right); break;
      case '-': nums.push(left - right); break;
      case '*': nums.push(left * right); break;
      case '/': nums.push(left / right); break;
    }
  }

  let i = 0;
  while (i < s.length) {
    if (s[i] >= '0' && s[i] <= '9') {//处理数字
      let value = 0;
      while (s[i] >= '0' && s[i] <= '9') {
        value = value * 10 + parseInt(s[i]);
        i++;
      }
      nums.push(value);
    } else if (s[i] == '(') {//碰到左括号近栈
      ops.push('(');
      i++;
    } else if (s[i] == ')') {//计算到最近的一个左括号为止
      while (ops[ops.length - 1] != '(') {
        calc();
      }
      ops.pop();//把左括号弹出
      i++;
    } else {//运算符
      if (ops.length == 0) {//栈为空时，遇到运算符，直接入栈
        ops.push(s[i]);
      } else if (map.get(s[i]) > map.get(ops[ops.length - 1])) {//当前运算符优先级高于之前的  5+2*3
        ops.push(s[i]);
      } else {//当前运算符优先级<=之前的  5*2-3
        do {
          calc();
        } while (map.get(s[i]) <= map.get(ops[ops.length - 1]));
        ops.push(s[i]);
      }
      i++;
    }
  }

  while (ops.length)
    calc();
  return nums[0];

}
module.exports = {
  solve: solve
};
