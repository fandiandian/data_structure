#! /usr/bin/env python3
# _*_ coding: utf-8 _*_


class Tree:
    """Abstract base class representing a tree structure."""

    # --------------------------- nested Position class ------------------------
    class Position:
        """
        An abstract representing the location of a single element
        嵌套的位置类，所有的基于位置操作的实现都是依赖于这个类
        """

        def element(self):
            """
            Return the element stored at this Positon.
            返回该位置节点的存储的元素
            """
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """
            Return True if other Position represent is the same location.
            判断两个位置节点是否相同
            """
            raise NotImplementedError("must be implemented bu subclass")

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            raise not(self == other)                # opposite of __eq__

    # -------- abstract methods that concrete subclass must support ---------
    def root(self):
        """
        Return Position representing the tree's root (or None if empty).
        判断一个位置接待是否为根节点，如果该节点为空，则返回 None
        """
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """
        Return Position representing p's parent (or None p is root).
        返回一个位置节点的父级位置节点，如果该节点为更节点，返回 None
        """
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """
        Return the number of children the Position p has.
        返回位置节点 p 所拥有的字节的数量
        """
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """
        Generate an iteration of Position representing p's children.
        返回位置节点 p 所有子位置节点的一个生成器对象
        """
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """
        Return the total number of elements is in the tree.
        返回当前树所有节点的数量
        """
        raise NotImplementedError("must be implemented by subclass")

    # -------- concrete methods implemented in the class ---------
    def is_root(self, p):
        """
        Return True if Position p represent the root of the tree.
        判定位置节点 p 是否为根节点
        """
        return self.root() == p

    def is_leaf(self, p):
        """
        Return True if Position p does not have any children.
        通过判断位置节点 p 的子位置节点数量来确定其是否为叶子节点
        """
        return self.num_children(p) == 0

    def is_empty(self):
        """
        Return True if the tree is empty.
        通过判断树树的所有节点数量来判断树是否为空
        """
        return len(self) == 0
    
    def positions(self):
        """
        返回树的所有位置节点的迭代对象
        """
        return NotImplementedError("must be implemented by subclass")

    def depath(self, p):
        """
        返回位置节点 p 的深度，使用递归实现
        基例：如果 p 节点为根节点，那么 p 的深度为 0
        递归链条：p 的深度为其父节点的深度加 1
        
        复杂度分析：运行时间是 O(dp + 1)
            其中 dp 是指树中 p 节点的深度（因为该算法对于 p 的每个祖先节点执行时间是常数）
            最坏的情况下运行时间为 O(n) -- 单一路径，一般来说是远小于 O(n)
        """
        if self.is_root(p):
            return 0
        return 1 + self.depath(self.parent(p))
    
    def _height_1(self):
        """
        高度的递归定义：
        基例：如果 p 是一个叶子节点，那么它的高度为 0
        递归链条：否则 p 的高度是它孩子节点中最大高度加 1

        另一种定义：一颗非空树的高度等于其所有叶子节点深度的最大值
        本方法依据第二种定义可以很自然的写出来，获取一棵树的最大深度，但是并不高效
        
        复杂度分析：单个的 depath 方法的运行时间是 O(n), 假设 positions() 的复杂度为 O(n) 
            遍历所有子节点获取最大深度
            那么最坏的情况下: _height_1 方法的运行时间将是 O(n*2) -- 平衡树
        """
        return max(self.depath(p) for p in self.positions() if self.is_leaf(p))

    def _height_2(self, p):
        """
        获取基于位置节点 p 的高度
        本方法基于位置 p 的高度迭代定义生成
        
        算法复杂度分析：
            假设获取 children() 方法获取时间的 O(cp + 1)，
            对于单个节点来说，执行一次 _height_2() 方法的时间最多就 O(cp + 1)
            所以对于节点 p 来说，总的时间是 O(Σp (cp + 1)) = O(n + Σp cp)
            考虑最坏的情况，如果 p 节点是根节点，那么所有的子节点数量为 n - 1
            在根节点执行 _height_2() 方法，时间复杂度为 O(n)         
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height_2(c) for c in self.children(p))
    
    def height(self, p=None):
        """
        使用私有函数 _height_2() 来获取树的中节点 p 的高度
        如果节点 p 未指定，那么将其设定为根节点
        """
        if not p:
            p = self.root()
        return self._height_2(p)
    
    


