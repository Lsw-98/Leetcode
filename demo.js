const count = 9
let res = 0
let multi = 1
for (let i = 0; i < 3; i++) {
  res += count * multi
  multi *= 10
}
console.log(res);