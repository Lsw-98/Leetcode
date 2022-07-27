/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  return s.split(" ").filter((item) => {
    return item !== ""
  }).reverse().join(" ")
};

console.log(reverseWords("  hello world!  "));