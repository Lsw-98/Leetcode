function bubbleSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    for (let j = 0; j < i + 1; j++) {
      if (arr[i] < arr[j]) {
        const temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
      }
    }
  }
  return arr
}

// 时间复杂度 O(n^2)

console.log(bubbleSort([1, 5, 9, 7, 3, 2, 6, 4, 8]))