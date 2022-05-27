function trans(s, n) {
  const arr = s.split(' ')
  arr.reverse()
  const res = []
  for (let i = 0; i < arr.length; i++) {
    const temp = arr[i].split('')
    res.push(temp)
  }
  for (let i = 0; i < res.length; i++) {
    for (let j = 0; j < res[i].length; j++) {
      if (res[i][j].charCodeAt() >= 65 && res[i][j].charCodeAt() <= 90) {
        res[i][j] = res[i][j].toLowerCase()
      } else {
        res[i][j] = res[i][j].toUpperCase()
      }
    }

  }
  for (let i = 0; i < res.length; i++) {
    res[i] = res[i].join('')

  }
  return res.join(' ')
}

module.exports = {
  trans: trans
}


console.log(trans("This is a sample", 16));
console.log(trans("nowcoder", 8));
console.log(trans("iOS", 3));
