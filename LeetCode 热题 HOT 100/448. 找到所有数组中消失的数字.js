// 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间[1, n] 内。请你找出所有在[1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果 

// 示例 1：
// 输入：nums = [4, 3, 2, 7, 8, 2, 3, 1]
// 输出：[5, 6]

// 示例 2：
// 输入：nums = [1, 1]
// 输出：[2]


/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function (nums) {
  let i = 0;
  while (i < nums.length) {
    if (nums[i] == i + 1) {
      i++;
      continue;
    }
    const idealIdx = nums[i] - 1;
    if (nums[i] == nums[idealIdx]) {
      i++;
      continue;
    }
    [nums[idealIdx], nums[i]] = [nums[i], nums[idealIdx]];
  }
  const res = [];
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != i + 1) {
      res.push(i + 1);
    }
  }
  return res;
};


console.log(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]));
console.log(findDisappearedNumbers([1, 1]));


// let arr = [1, 2, 3, 4]
// arr[arr.indexOf(4)] = 0
// console.log(arr);