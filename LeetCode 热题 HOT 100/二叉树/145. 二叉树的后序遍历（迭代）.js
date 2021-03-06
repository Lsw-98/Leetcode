/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var postorderTraversal = function (root) {
    let res = []
    if (root === null) return res
    const stack = []
    stack.push(root)

    while (stack.length) {
        const temp = stack.pop()
        res.push(temp.val)
        if (temp.left) {
            stack.push(temp.left)
        }
        if (temp.right) {
            stack.push(temp.right)
        }
    }
    res = res.reverse()
    return res
};