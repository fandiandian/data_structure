#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
这个是二叉树的抽象基类，及继承自树的抽象基类
增加三种特殊的访问方法
T.left(p): 返回位置节点 p 的左孩子节点，若 p 没有左孩子节点，则返回 None
T.right(p): 同 left 方法一样，返回的是右孩子节点
T.sibling(p): 返回位置节点 p 的兄弟节点，如果没有兄弟节点，则返回 None

二叉树的特性：
    每层的节点数量最多为 2 ** d 个 -- d 为当前层数（根节点为 0 层）
    非空完全二叉树中，外部节点比内部节点多 1
"""

from adt_of_tree import Tree


class BinaryTree(Tree):
    """
    二叉树的抽象基类
    """

    # ---------------- 新增的两种抽象访问方法 -------------------
    def left(self, p):
        """
        返回位置节点 p 的左孩子节点，如果没有则返回 None
        """
        return NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """
        返回位置节点 p 的右孩子节点，如果没有则返回 None
        """
        return NotImplementedError("must be implemented by subclass")
    
    # ---------------- 新增的两种具体实现的访问方法 -------------------
    def sibling(self, p):
        """
        返回位置节点 p 的兄弟节点，如果没有则返回 None
        """
        parent = self.parent(p)
        if parent is None:              # p 节点为 root 节点
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    
    def children(self, p):
        """
        实现父类 Tree 中的 children 方法
        返回位置节点 p 的孩子节点的生成器
        返回的孩子节点的顺序是从左往右
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

