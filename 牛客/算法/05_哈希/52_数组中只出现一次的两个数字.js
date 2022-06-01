/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param array int整型一维数组 
 * @return int整型一维数组
 */
function FindNumsAppearOnce(array) {
  const values = []
  const index = []
  const res = []

  for (let i = 0; i < array.length; i++) {
    if (index.includes(array[i])) {
      values[index.indexOf(array[i])] += 1
    } else {
      index.push(array[i])
      values.push(1)
    }
  }

  console.log(values);

  for (let i = 0; i < values.length; i++) {
    if (values[i] === 1) {
      res.push(index[values.indexOf(values[i])])
      values[i] = -1
    }
  }
  return res.sort()
}
module.exports = {
  FindNumsAppearOnce: FindNumsAppearOnce
};


console.log(FindNumsAppearOnce([1, 4, 1, 6]));