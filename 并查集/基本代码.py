"""

并查集用于判断一堆元素是否相连,他们的关系是动态添加的，这一类问题叫做“动态连通性”问题
主要支持 合并 与 查询是否在同一集合 的操作
底层结构是 数组 或 哈希表 ，用于表示 结点 指向的 父节点 ，初始化时指向自己
合并 就是把一个集合的根结点指向另一个集合的根节点，只要根节点一样，就表示在同一个集合里
这种表示 不相交集合 的方法称之为 “代表元法”，一每个结点的根节点作为一个集合的 代表元

应用：最小生成树: kruskal算法

"""


class UnionFindSet(object):

    def __init__(self, nodes):
        '''
        初始化并查集
        :param nodes: 传入的数据
        '''
        # 记录每个节点的父节点
        self.fatherMap = {}
        # 各门派的人数
        self.setNumMap = {}
        # 初始化, 每个节点自成一派
        for node in nodes:
            self.fatherMap[node] = node
            self.setNumMap[node] = 1

    def findFather(self, node):
        '''
        递归逻辑:返回当前节点的父节点; base case:当前节点的父节点是自己
        :param node:
        :return:
        '''
        father = self.fatherMap[node]
        if (node != father):
            father = self.findFather(father)
        # 超级优化: 路径压缩
        self.fatherMap[node] = father
        return father

    def isSameSet(self, a, b):
        '''
        判断两个节点a和b是否属于同一门派
        :param a:
        :param b:
        :return:
        '''
        return self.findFather(a) == self.findFather(b)

    def union(self, a, b):
        '''
        合并a所在的门派和b所在的门派
        :param a:
        :param b:
        :return:
        '''
        if a is None or b is None:
            return
        # a的掌门
        aFather = self.findFather(a)
        # b的掌门
        bFather = self.findFather(b)

        if (aFather != bFather):
            # a所在门派的人数
            aNum = self.setNumMap[aFather]
            # b所在门派的人数
            bNum = self.setNumMap[bFather]
            # 人数少的门派加入人数多的门派
            if (aNum <= bNum):
                self.fatherMap[aFather] = bFather
                self.setNumMap[bFather] = aNum + bNum
                # aFather不再是掌门人了, 删除aFather对应的人数纪录
                self.setNumMap.pop(aFather)
            else:
                self.fatherMap[bFather] = aFather
                self.setNumMap[aFather] = aNum + bNum
                # bFather不再是掌门人了, 删除bFather对应的人数纪录
                self.setNumMap.pop(bFather)


if __name__ == '__main__':
    nodes = ['剑魂', '红眼', '漫游', '元素', '魔道', '战法', '大枪', '散打', '弹药', '机械']
    union_find = UnionFindSet(nodes)
    union_find.union('剑魂', '红眼')
    union_find.union('漫游', '大枪')
    union_find.union('漫游', '弹药')
    union_find.union('漫游', '机械')
    union_find.union('元素', '魔道')
    union_find.union('元素', '战法')

    print(union_find.isSameSet('大枪', '弹药'))  # True
    print(union_find.isSameSet('剑魂', '战法'))  # False
    print(union_find.isSameSet('魔道', '散打'))  # False
    print(union_find.isSameSet('魔道', '战法'))  # True

