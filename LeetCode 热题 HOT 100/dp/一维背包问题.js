const weight = [1, 3, 4]
const value = [15, 20, 30]
const bagweight = 4

let dp = Array(bagweight + 1).fill(0);

for (let i = 1; i <= weight.length; i++) {
  for (let j = bagweight; j >= weight[i - 1]; j--) {
    dp[j] = Math.max(dp[j], dp[j - weight[i - 1]] + value[i - 1])
  }
}

console.log(dp[bagweight]);