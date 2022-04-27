// 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
// 给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。


// 示例 1：
// 输入：flowerbed = [1, 0, 0, 0, 1], n = 1
// 输出：true

// 示例 2：
// 输入：flowerbed = [1, 0, 0, 0, 1], n = 2
// 输出：false


/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {
  if (flowerbed.length === 1) {
    if (flowerbed[0] === 0) {
      return true
    } else {
      return false
    }
  }
  while (n) {
    for (let index = 0; index < flowerbed.length; index++) {
      if (index === 0) {
        if (flowerbed[index] === 0 && flowerbed[index + 1] === 0) {
          flowerbed[index] = 1
          n -= 1
        }
      } else if (0 < index && index < flowerbed.length - 1) {
        if (flowerbed[index - 1] === 0 && flowerbed[index] === 0 && flowerbed[index + 1] === 0) {
          flowerbed[index] = 1
          n -= 1
        }
      } else {
        if (flowerbed[index - 1] === 0 && flowerbed[index] === 0) {
          flowerbed[index] = 1
          n -= 1
        }
      }

    }
    if (n > 0) {
      return false
    } else {
      return true
    }
  }
  return true
};


console.log(canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2));
console.log(canPlaceFlowers([1, 0, 0, 0, 1], 2));
