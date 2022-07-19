let result = [],
  line = 90;

for (let i = 2; i <= line; i++) { // 2是最小的质数，所以从2开始找
  if (line % i === 0) { // 找到了质因数中最小的质数i
    line = line / i; // 从整除结果中继续寻找该结果的最小质数
    result.push(i);
    i = 1; // 还是从最小质数2开始寻找，因为i有一个++操作，所以这里是1
  }
}
console.log(result);