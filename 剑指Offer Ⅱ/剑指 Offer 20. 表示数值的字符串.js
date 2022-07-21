/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function (s) {
  s = s.split("")
  for (let i = 0; i < s.length; i++) {
    if (i === ".") {

    }
  }
};

console.log(isNumber("0"));
console.log(isNumber("e"));
console.log(isNumber("."));
console.log(isNumber("    .1  "));
console.log(isNumber("+100"));
console.log(isNumber("5e2"));
console.log(isNumber("-123"));
console.log(isNumber("3.1416"));
console.log(isNumber("-1E-16"));
console.log(isNumber("0123"));
console.log(isNumber("12e"));
console.log(isNumber("1a3.14"));
console.log(isNumber("1.2.3"));
console.log(isNumber("+-5"));
console.log(isNumber("12e+5.4"));
