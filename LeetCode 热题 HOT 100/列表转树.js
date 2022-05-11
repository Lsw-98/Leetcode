const list = [
  { key: 1, value: "one", parentKey: 0 },
  { key: 2, value: "two", parentKey: 0 },
  { key: 3, value: "three", parentKey: 1 },
  { key: 4, value: "four", parentKey: 2 },
  { key: 5, value: "five", parentKey: 2 },
  { key: 6, value: "six", parentKey: 3 },
  { key: 7, value: "seven", parentKey: 4 },
  { key: 8, value: "eight", parentKey: 3 },
]

function getTree(list) {
  let res = []
  for (let i = 0; i < list.length; i++) {
    if (list[i].parentKey === 0) {
      list[i].children = []
      res.push(list[i])
    } else if (list[i].parentKey === 1) {
      res[0].children.push(list[i])
    }
  }
  return res
}

const res = getTree(list)
console.log(res);