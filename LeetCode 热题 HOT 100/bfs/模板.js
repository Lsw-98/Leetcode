/**
 * BFS 使用队列，把每个还没有搜索到的点依次放入队列，然后再弹出队列的头部元素当做当前遍历点。
 */

// 1. 如果不需要确定当前遍历到哪一层
while (queue不空) {
  cur = queue.pop()
  for (const 节点 of cur的相邻节点) {
    if (该节点有效且未访问过) {
      queue.push(该节点)
    }
  }
}

// 2. 如果要确定当前遍历到了哪一层
/**
 * 这里增加了level表示当前遍历到二叉树中的哪一层，也可以理解为在一个图中，现在已经走了多少步了
 * size表示当前遍历曾有多少个元素，也就是队列中的元素数，
 * 把这些元素一次性遍历完，即把当前层的所有元素都向外走了一步
 */

level = 0
while (queue不空) {
  size = queue.length
  for (; size > 0; size--) {
    cur = queue.pop()
    for (const 节点 of cur) {
      if (节点未被访问过且有效) {
        queue.push(该节点)
      }
    }
  }
  level += 1
}

// 快速生成二维数组
let dp = new Array(3).fill(0).map(() => {
  return new Array(3).fill(0)
});