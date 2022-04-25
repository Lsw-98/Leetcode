// 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。

// 示例 1:
// 输入：inorder = [9, 3, 15, 20, 7], postorder = [9, 15, 7, 20, 3]
// 输出：[3, 9, 20, null, null, 15, 7]

// 示例 2:
// 输入：inorder = [-1], postorder = [-1]
// 输出：[-1]


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function (inorder, postorder) {
  /**
   * 思路：
   * 第一步：如果数组大小为零的话，说明是空节点了。
   * 第二步：如果不为空，那么取后序数组最后一个元素作为节点元素。
   * 第三步：找到后序数组最后一个元素在中序数组的位置，作为切割点
   * 第四步：切割中序数组，切成中序左数组和中序右数组 （顺序别搞反了，一定是先切中序数组）
   * 第五步：切割后序数组，切成后序左数组和后序右数组
   * 第六步：递归处理左区间和右区间
   */

  // 框架
  /**
   * 
    TreeNode* traversal (vector<int>& inorder, vector<int>& postorder) {

      // 第一步
      if (postorder.size() == 0) return NULL;

      // 第二步：后序遍历数组最后一个元素，就是当前的中间节点
      int rootValue = postorder[postorder.size() - 1];
      TreeNode* root = new TreeNode(rootValue);

      // 叶子节点
      if (postorder.size() == 1) return root;

      // 第三步：找切割点
      int delimiterIndex;
      for (delimiterIndex = 0; delimiterIndex < inorder.size(); delimiterIndex++) {
          if (inorder[delimiterIndex] == rootValue) break;
      }

      // 第四步：切割中序数组，得到 中序左数组和中序右数组
      // 第五步：切割后序数组，得到 后序左数组和后序右数组

      // 第六步
      root->left = traversal(中序左数组, 后序左数组);
      root->right = traversal(中序右数组, 后序右数组);

      return root;
    }
   */

  // 第一步：判断数组是否为空
  if (inorder.length === 0) return null

  // 第二步，取后序遍历的最后一个节点
  const rootVal = postorder.pop()

  // 第三步，获取中间节点在中序遍历中的下标
  let rootIndex = inorder.indexOf(rootVal)

  // 创建中间节点
  const root = new TreeNode(rootVal)

  // 递归切割的数组
  root.left = buildTree(inorder.slice(0, rootIndex), postorder.slice(0, rootIndex))
  root.right = buildTree(inorder.slice(rootIndex + 1), postorder.slice(rootIndex))

  return root
};