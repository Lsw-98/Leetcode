/**
 * @param {string} s
 * @return {string}
 */
var replaceSpace = function (s) {
  const res = s.split(" ")
  return res.join("%20")
};