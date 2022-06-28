/* function TreeNode(x) {
    this.val = x;
    this.left = null;
    this.right = null;
} */
function Convert(pRootOfTree) {
  let head = null;
  let pre = null;
  function MediumOrderDFS(cur) {
    if (cur === null) {
      return;
    }
    // 递归左结点
    MediumOrderDFS(cur.left);
    // 处理当前结点
    if (pre === null) {
      head = cur;
    } else {
      pre.right = cur;
    }
    cur.left = pre;
    pre = cur;
    // 遍历右结点
    MediumOrderDFS(cur.right);
  }
  MediumOrderDFS(pRootOfTree);
  return head;
}
module.exports = {
  Convert: Convert
};