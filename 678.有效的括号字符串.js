/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function (s) {
  const left = [];
  let star = [];
  for (let i = 0; i < s.length; i++) {
    if (!s[i]) continue;
    if (s[i] === '*') star.push(i);
    if (s[i] === '(') left.push(i);
    if (s[i] === ')') {
      if (!left.length) {
        if (!star.length) return false;
        star.pop();
      }
      else left.pop(s[i]);
    }
  }
  const temp = [];
  let j = 0, k = 0;
  for (let i = 0; i < s.length; i++) {
    if (i === left[j]) {
      temp.push(i);
      j++;
    }
    else if (i === star[k]) {
      temp.pop();
      k++;
    }
  }
  return !temp.length;
};

console.log(checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"));
console.log(checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"));
console.log(checkValidString("(((()))())))*))())()(**(((())(()(*()((((())))*())(())*(*(()(*)))()*())**((()(()))())(*(*))*))())"));
