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
var preorderTraversal = function (root) {
    res = []
    function getVal(root) {
        if (root !== null) {
            res.push(root.val)
            getVal(root.left)
            getVal(root.right)
        }
    }

    getVal(root)
    return res
};