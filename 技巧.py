'''

    # 二分求mid的方法： left + (right - left) // 2

    # 先按照左端点升序排序，如果左端点相同，则按照右端点降序排序
    temp.sort(key=lambda x: [x[0], -x[1]])

    1 字符串反转

　　使用切片反转字符串。

　　str1="qwert"
   rev_str1=str1[::-1] #输出 # trewq

　　2 使首字母大写

　　将字符串转换为首字母大写。使用 title()方法完成的。

　　str1="this is a book"
   print(str1.title()) # This Is A Book

　　3 在字符串中查找唯一元素

　　下面代码可用于查找字符串中所有的唯一元素。

　　str1="aabbccccdddd"
   set1=set(str1)
   new_str=''.join(set1)
   print(new_str)

　　4 重复打印字符串或列表

　　下面的代码中，对字符串或列表使用(*)。把字符串或列表复制多次。

　　i=4
   str1="abcd"
   list1=[1,2]
   print(str1*i) # abcdabcdabcdabcd print(list1*i) # [1,2,1,2,1,2,1,2]

　　5 列表推导式

　　列表推导式为我们提供了一种在其他列表基础上创建列表的好方法。下面代码通过将旧列表的每个元素乘以 2 来创建新列表。

　　list1=[1,2,3]
   new_list1=[2*i for i in list1] # [2,4,6]

　　6 交换变量

　　不使用另一个变量，实现变量交换。

　　 x=1
    y=2
    x,y=y,x
    print(x) # 2
    print(y) # 1

　　7 将字符串拆分为子字符串列表

　　我们使用字符串类中的.split()方法将字符串拆分为子字符串列表，还可以将要分割的分隔符作为参数传递。

　　str1="This is a book"str2="test/ str 2"print(str1.split()) # ['This', 'is', 'a', 'book'] print(str2.split('/')) # ['test', ' str 2']

　　8 将字符串列表组合成单个字符串

　　join()将作为参数传递的字符串列表组合为单个字符串。这种情况下，我们使用逗号分隔符将它们分开。

　　list_str=['This','is','a','book']print(','.join(list_str))# This,is,a,book

　　9 检查回文字符串

　　我们已经讨论过如何反转字符串，因此回文字符串在 Python 中判断起来非常简单。

　　str1="qqaabb"
    if str1==str1[::-1]: print("回文")else: print("不是") # 不是

　　10 列表中的元素统计

　　使用 Python Counter 类。Python 计数器跟踪容器中每个元素的频数， Counter()返回一个字典，元素作为键，频数作为值。

　　另外使用 most_common()函数来获取列表中的 出现次数最多的元素。

　　from collections import Counter
    list1=['a','b','a','c','c','c']
    count=Counter(list1)
    print(count)
    print(count['b'])
    print(count.most_common(1))

　　11 判断两个字符串是否为异序词

　　异序词是通过重新排列不同单词或短语的字母而形成的单词或短语。如果两个字符串的 Counter 对象相等，那么它们就是相同字母异序词对。

　　s1,s2,s3="acbde","abced","abcda"
    c1,c2,c3=Counter(s1),Counter(s2),Counter(s3)
    if c1==c2: print('1和2是异序词')
    if c1==c3: print('1和3是异序词')

　　12 使用 try-except-else 块

　　try / except 是 Python 中的异常处理模块，添加 else 语句，会在 try 块中没有引发异常的情况下运行。

　　a,b=1,0try: print(a/b) # b为0的时候触发异常except ZeroDivisionError: print("除数为0")else: print("不存在异常")finally: print("此段总是会执行")

　　13 通过枚举获取索引 / 值对

　　可以使用下面的脚本，遍历列表中的值及其索引。

　　list1=['a','b','c','d','e']
    for idx,val in enumerate(list1): print('{0}:{1}'.format(idx,val))# 0:a# 1:b# 2:c# 3:d# 4:e

　　14 获取对象的内存使用信息

　　下面脚本可用于检查对象的内存使用信息。

　　import sysnum=21print(sys.getsizeof(num))

　　15 合并两个字典

　　在 Python 2 中，使用 update()合并两个字典，Python 3 变得更加简单。

　　下面脚本中，两个字典被合并。
    在相交的情况下，使用第二个字典中的值。

　　dic1={'app':9,'banana':6}
    dic2={'banana':4,'orange':8}
    com_dict={**dic1,**dic2}   # {'apple':9,'banana':4,'orange':8}

　　16 计算代码执行所需的时间

　　下面代码使用库函数来计算执行代码所需的时间消耗多少毫秒。
　　import times_time=time.time()
    a,b=1,2
    c=a+b
    e_time=time.time()time_taken_in_micro=(e_time-stime)*(10**6)
    print("程序运行的毫秒：{0} ms".format(time_taken_in_micro))

　　17 展开列表清单

　　有时不知道列表的嵌套深度，并且只想把所有元素放在一个普通列表中。可以通下面的方法得到数据：

　　from iteration_utilities import deepflatten
# 如果嵌套列表的深度只有1层
    def flatten(l):
    return [item for sublist in l for item in sublist]l=[[1,2,3],[3]]
    print(flatten(l))# [1,2,3,3]
# 如果不知道列表嵌套深度
    l=[[1,2,3],[4,[5],[6,7]],[8,[9,[10]]]]
    print(list(deepflatten(l,depth=3)))
    # [1,2,3,4,5,6,7,8,9,10]

　　18 从列表中随机取样

　　下面代码从给定列表中生成了 n 个随机样本。

　　import random
    list1=['a','b','c','d','e']
    ns=2
    samples=random.sample(list1,ns)
    print(samples)# ['a','c']

　　或者使用secrets库生成随机样本进行， 下面代码仅适用于 Python 3.x。

　　import secrets
    s_rand=secrets.SystemRanom()
    list1=['a','b','c','d','e']
    ns=2
    samples=s_rand.sample(list1,ns)
    print(samples)# ['c','d']

　　19 数字列表化

　　下面代码将整数转换为数字列表。

　　nums=123456
    # 使用map
    digit_list=list(map(int,str(nums)))
    print(digit_list)    # [1,2,3,4,5,6]
    # 使用列表表达式
    digit_list=[int(x) for x in str(nums)]
    print(digit_list)    # [1,2,3,4,5,6]

　　20 唯一性检查

　　下面的函数检查列表中的元素是否唯一。

　　def unique(l):
        if len(l)==len(set(l)):
            print("所有元素是唯一的")
        else:
            print("存在重复")
    unique([1,2,3,4]) # 所有元素是唯一的
    unique([1,1,3,4]) # 存在重复`

'''


# 判断素数
# n = int(input())
# sum = 0
# for i in range(2, n + 1):
#     # 设置一个flag,默认为False，即不是素数
#     flag = False
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             flag = True
#             break
#     if not flag:
#         sum += i
# print(sum)


# 用最大公约数以及辗转相除法求最小公倍数
# 两个数
# m, n = map(int, input().split())
# if n > m:
#     m, n = n, m
# muti = m * n
# x = m % n
# while x:
#     m = n
#     n = x
#     x = m % n
# print("最大公约数是:", n)
# print("最小公倍数时:", muti // n)


# 三个数
# 计算三个数时先求出两个数的最小公倍数，在和另一个数求最小公倍数
# def gcm(x, y):
#     if x < y:
#         x, y = y, x
#     xy_mod = x % y
#     while xy_mod != 0:
#         y = xy_mod
#         x = y
#         xy_mod = x % y
#     return y
#
#
# def lcm(x, y):
#     return int(x * y / gcm(x, y))


# a, b, c = map(int, input().split(' '))
# ab_lcm = lcm(a, b)
# print(lcm(ab_lcm, c))

# 约瑟夫环问题
# 基本问题描述：
# 已知n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。
# 从编号为1的人开始报数，数到m的那个人出列；他的下一个人又从1开始报数，数到m的那个人又出列；
# 依此规律重复下去，直到圆桌周围的人全部出列。（也类似于变态杀人狂问题）通常解决这类问题时我们把编号从0~n-1，
# 最后结果+1即为原问题的解。

# def josephus(n, k):
#     if k == 1:
#         print('survive:', n)
#         return
#     p = 0
#     people = list(range(1, n + 1))
#     while True:
#         if len(people) == 1:
#             break
#         p = (p + (k - 1)) % len(people)
#         print('kill:', people[p])
#         del people[p]
#     print('survive:', people[0])

# if __name__ == '__main__':
#     josephus(10, 4)
#     josephus(10, 2)
#     josephus(10, 1)


"""
二叉树和它的7种遍历
"""

"""
# class Node(object):
#     # 节点类: 初始化一个节点,需要为节点设置值
#     def __init__(self, val):
#         self.val = val
#         self.lchild = None
#         self.rchild = None
# 
# 
# class BinaryTree(object):
#     # 树类
#     def __init__(self):
#         self.root = None
# 
#     # 为树添加节点
#     def addNode(self, val):
#         # 创建队列存储节点
#         nodeStack = [self.root]
# 
#         # 如果树为空，则对根节点赋值
#         if not self.root:
#             self.root = Node(val)
#             print("添加根节点{0}成功!".format(self.root.val))
#             return
# 
#         while len(nodeStack) > 0:
#             # 队列元素出列
#             pop_node = nodeStack.pop()
# 
#             # 如果左结点为空
#             if not pop_node.lchild:
#                 pop_node.lchild = Node(val)
#                 print("添加左结点:{0} ".format(pop_node.lchild.val))
#                 return
# 
#             # 如果右结点为空
#             if not pop_node.rchild:
#                 pop_node.rchild = Node(val)
#                 print("添加右结点:{0} ".format(pop_node.rchild.val))
#                 return
# 
#             # 这里为什么先插入左再插入右呢？
#             nodeStack.insert(0, pop_node.lchild)
#             nodeStack.insert(0, pop_node.rchild)
# 
#     # 广度：层次
#     def breadthFirst(self):
#         nodeStack = [self.root]
# 
#         while len(nodeStack) > 0:
#             my_node = nodeStack.pop()
#             print(my_node.val, "-->", end='')
# 
#             if my_node.lchild:
#                 nodeStack.insert(0, my_node.lchild)
# 
#             if my_node.rchild:
#                 nodeStack.insert(0, my_node.rchild)
# 
#     # 深度：先中后
#     def preorder(self, start_node):
#         if not start_node:
#             return
#         print(start_node.val, end=' ')
#         self.preorder(start_node.lchild)
#         self.preorder(start_node.rchild)
# 
#     def inorder(self, start_node):
#         if not start_node:
#             return
#         self.inorder(start_node.lchild)
#         print(start_node.val, end=' ')
#         self.inorder(start_node.rchild)
# 
#     def lastorder(self, start_node):
#         if not start_node:
#             return
#         self.lastorder(start_node.lchild)
#         self.lastorder(start_node.rchild)
#         print(start_node.val, end=' ')
# 
# 
# def main():
#     bt = BinaryTree()
#     bt.addNode(0)
#     bt.addNode(1)
#     bt.addNode(2)
#     bt.addNode(3)
#     bt.addNode(4)
#     bt.addNode(5)
#     bt.addNode(6)
#     bt.addNode(7)
#     bt.addNode(8)
#     bt.addNode(9)
# 
#     print("广度遍历: ", end='')
#     bt.breadthFirst()
#     print()
# 
#     print("先序遍历: ", end='')
#     bt.preorder(bt.root)
#     print()
# 
#     print("中序遍历: ", end='')
#     bt.inorder(bt.root)
#     print()
# 
#     print("后序遍历: ", end='')
#     bt.lastorder(bt.root)
# 
# 
# if __name__ == '__main__':
#     main()

"""


"""
class Node(object):
    # 节点类

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    # 树类

    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        # 为树添加节点
        node = Node(elem)
        if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。

    def front_digui(self, root):
        # 利用递归实现树的先序遍历
        if root == None:
            return
        print(root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self, root):
        # 利用递归实现树的中序遍历
        if root == None:
            return
        self.middle_digui(root.lchild)
        print(root.elem)
        self.middle_digui(root.rchild)

    def later_digui(self, root):
        # 利用递归实现树的后序遍历
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print(root.elem)

    def front_stack(self, root):
        # 利用堆栈实现树的先序遍历
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                print(node.elem)
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.rchild  # 开始查看它的右子树

    def middle_stack(self, root):
        # 利用堆栈实现树的中序遍历
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            print(node.elem)
            node = node.rchild  # 开始查看它的右子树

    def later_stack(self, root):
        # 利用堆栈实现树的后序遍历
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:  # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:  # 将myStack2中的元素出栈，即为后序遍历次序
            print(myStack2.pop().elem)

    def level_queue(self, root):
        # 利用队列实现树的层次遍历
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem)
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)


if __name__ == '__main__':

    elems = range(10)  # 生成十个数据作为树节点
    tree = Tree()  # 新建一个树对象
    for elem in elems:
        tree.add(elem)  # 逐个添加树的节点

    print('队列实现层次遍历:', tree.level_queue(tree.root))

    print('\n\n递归实现先序遍历:', tree.front_digui(tree.root))

    print('\n递归实现中序遍历:', tree.middle_digui(tree.root))

    print('\n递归实现后序遍历:', tree.later_digui(tree.root))

    print('\n\n堆栈实现先序遍历:', tree.front_stack(tree.root))

    print('\n堆栈实现中序遍历:', tree.middle_stack(tree.root))

    print('\n堆栈实现后序遍历:', tree.later_stack(tree.root))

"""

"""
使用树状数组进行区间修改，区间查询，单间查询，单点更新

# 博文地址，讲的很好
# https://www.cnblogs.com/xenny/p/9739600.html
"""

# 树状数组可以解决的问题
# 可以解决大部分基于区间上的更新以及求和问题

# 树状数组和线段树的区别在哪里
# 树状数组的系数要少很多，就比如字符串模拟大数可以解决大数问题，也可以解决1+1的问题

# 树状数组的优点和缺点
# 修改和查询的复杂度都是O(logN)，
# 而且相比线段树系数要少很多，比传统数组要快，而且容易写。
# 缺点是遇到复杂的区间问题还是不能解决，功能还是有限。


"""
这里没懂C[7]怎么算
"""
# C[i] = A[i - 2^k+1] + A[i - 2^k+2] + ... + A[i]
# 对于每一个C[n]他的父亲都是C[nn] (nn=n + 2^k)
# k为i的二进制中从最低位到高位连续零的长度
# 2^k = i&(-i)
# x&(-x)，
# 当x为0时结果为0；
# x为奇数时，结果为1；
# x为偶数时，结果为x中2的最大次方的因子

"""
区间求和SUM即为：SUMi = C[i] + C[i-2^k1] + C[(i - 2^k1) - 2^k2] + .....
"""

"""
单点更新
"""
# 上面说了C[i] = A[i - 2^k+1] + A[i - 2^k+2] + ... + A[i]，
# 那么如果我们更新某个A[i]的值，则会影响到所有包含有A[i]位置。
# 如果求A[i]包含哪些位置里呢，同理有
# A[i] 包含于 C[i + 2^k]、C[(i + 2^k) + 2^k]...；

"""
复现代码
"""


def lowbit(x):
    return x & (-x)


# 在i位置上加k
def update(index, k):
    while index <= n:
        tree[index] += k
        index += lowbit(index)


# 求前i项和
def getsum(i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= lowbit(i)
    return res


n, m = map(int, input().split())
# 控制台输入的数组
temp = list(map(int, input().split()))
# 原数组
original = []
# 树状数组
tree = [0 for i in range(n)]
# 将temp数组的前n位放入original数组中
for x in range(n):
    original.append(temp[x])
    update(x, original[x])
print(original)
print(tree)


# 各种操作
# for j in range(1, m + 1):
#     temp = list(map(int, input().split()))
#     if temp[0] == 1:
#         pass
#     elif temp[0] == 2:
#         pass
#     else:
#         pass






# 贪心算法
# # 实现数字拼接问题
# from functools import cmp_to_key
#
#
# def xy_cmp(x, y):
#     if x + y < y + x:
#         return 1
#     elif x + y > y + x:
#         return -1
#     else:
#         return 0
#
#
# def number_join(li):
#     li = list(map(str, li))
#     li.sort(key=cmp_to_key(xy_cmp))
#     return "".join(li)
#
#
# print(number_join([32, 94, 728, 7286, 6, 71]))
# print(number_join([32, 94, 128, 1286, 6, 71]))


# 活动选择问题
# 最先结束的活动一定是最优解的一部分

# 活动时间
# 保证活动时间是按照结束时间排好序的


# def activities_selection(activities):
#     activities.sort(key=lambda x: x[1])
#     res = [activities[0]]
#     for i in range(1, len(activities)):
#         if activities[i][0] >= res[-1][1]:
#             res.append(activities[i])
#     return res


# print(activities_selection([(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]))


# 快速幂
# def power(base, exponent):
#     res = 1
#     while exponent:
#         if exponent & 1:  # 判断当前的最后一位是否为1，如果为1的话，就需要把之前的幂乘到结果中。
#             res *= base
#         base *= base  # 一直累乘，如果最后一位不是1的话，就不用了把这个值乘到结果中，但是还是要乘。
#         exponent = exponent >> 1
#     return res


# 斐波那契数列
# 矩阵乘法
# 快速幂
# 模的加减乘除运算
# (a + b) % p = (a % p + b % p) % p
# ( a − b ) % p = ( a % p − b % p ) % p
# ( a ∗ b ) % p = ( a % p ∗ b % p ) % p

# 定义二阶矩阵的相乘
# def multi(a, b):
#     towd_matrix = [[0, 0], [0, 0]]
#     for i in range(2):
#         for j in range(2):
#             for k in range(2):   # 新的二阶矩阵的值计算
#                 towd_matrix[i][j] = towd_matrix[i][j] + a[i][k] * b[k][j]
#     return towd_matrix
#
#
# def matrix(n):
#     # 定义元矩阵
#     base = [[1, 1], [1, 0]]
#     # 结果矩阵
#     ans = [[1, 0], [0, 1]]
#     while n:
#         if n & 1:
#             ans = multi(ans, base)
#         base = multi(base, base)
#         n >>= 1
#     # 最后二阶矩阵的[0][1]即为fn的值
#     return ans[0][1]
#
#
# print(matrix(10))

# 快速求大数的Cnm组合问题
# 同余定理: 给定一个正整数m，如果两个整数a和b满足a - b能够被m整除，即(a - b) / m得到一个整数，
# 那么就称整数a与b对模m同余，记作a≡b mod m。对模m同余是整数的一个等价关系。
#
# 逆元：对于a和p，若a和p互素且
# ( a ∗ b ) % p ≡ 1
# 则称b为a % p的逆元。
# 假设c为b % p的逆元，即b ∗ c % p = 1
# (a / b) % p = (a % p) ∗ (c % p) % p
# 这样就把求( a / b ) % p转化成一个( a % p ) ∗ ( c % p ) % p 乘法问题。




# 动态规划
# 状态转移方程
# 动态规划要从小问题入手，逐步解决大问题

# 斐波那契数列
# def Fibonacci(n):
#     f1 = 1
#     f2 = 1
#     for i in range(2, n + 1):
#         f2 += f1
#         f1 = f2 - f1
#     return f1
#
# print(Fibonacci(100))


# 钢条切割问题
# 某公司出售钢条，出售价格和钢条长度之间关系如下：
# 长度  1   2   3   4   5   6   7   8   9   10
# 价格  1   5   8   9   10  17  17  20  24  30
# 问题: 现有一段长度为n的钢条吗，求切割钢条方案，使得收益最大


# 01背包问题
# 给定 n 件物品，物品的重量为 w[i]，物品的价值为 c[i]。
# 现挑选物品放入背包中，假定背包能承受的最大重量为 V，
# 问应该如何选择装入背包中的物品，使得装入背包中物品的总价值最大？
def pack(weight, value, w):
    block = [[0] * (w + 1) for _ in range(len(weight) + 1)]

    if len(weight) == 0:
        return 0
    else:
        for j in range(1, len(weight) + 1):
            for k in range(1, w + 1):
                temp_goods = 0
                temp_not_goods = 0

                # 关键步骤，状态转移方程
                # 存放j号物品(前提是放得下j号物品)
                if k - weight[j - 1] >= 0:
                    temp_goods = value[j - 1] + block[j - 1][k - weight[j - 1]]
                # 不存放j号物品
                temp_not_goods = block[j - 1][k]
                block[j][k] = max(temp_goods, temp_not_goods)

    return block[-1][-1]


# 最大最小值动态规划问题(求最值形的的动态规划)
# 基本思路: 最优策略肯定是有k枚硬币a1, a2, ..., ak的面值和为amount
# 所以一定有最后一枚硬币ak, 除掉这枚硬币, 前面的硬币面值为amount - ak
#
# def coinChange(coins, amount):
#     f = [float('inf') for i in range(amount + 1)]
#     f[0] = 0
#     for j in range(1, amount + 1):
#         for k in range(len(coins)):
#             if (j >= coins[k]) and (f[j - coins[k]] != float('inf')):
#                 # f[j] = f[j - coins[k]] + 1
#                 f[j] = min(f[j - coins[k]] + 1, f[j])
#     if f[amount] == float('inf'):
#         f[amount] = -1
#     return f[-1]
