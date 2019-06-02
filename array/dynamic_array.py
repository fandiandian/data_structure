#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
基于 ctypes 模块实现的动态数组

关于 ctypes 模块 -- 官方文档
ctypes 是 Python 的外部函数库。它提供了与 C 兼容的数据类型，并允许调用 DLL 或共享库中的函数。可使用该模块以纯 Python 形式对这些库进行封装。
目前的水平有限，还无法理解这个模块

在此处，使用 ctypes 模块构建一个固定长度的数组（原始数组）
"""

import ctypes


class DynamicArray:
    """
    一个动态的数组类，类似于简单化的 Python 列表
    """

    def __init__(self):
        """
        创建一个空的数组
        """
        # 数组用元素数量的计数器 -- 内存空间的实际使用量 -- <逻辑大小>
        self._n = 0
        # 默认的数组大小为 1 -- 划分的内存空间大小 -- <物理大小>                                  
        self._capacity = 1                          
        self._A = self._make_array(self._capacity)       # 低层次的原始数组

    def __len__(self):
        """
        返回数组的长度（数组中存储元素的数量）
        """
        return self._n

    def __getitem__(self, k):
        """
        返回数组下表索引 k 对应的元素
        """
        if not 0 <= k < self._n:
            raise IndexError("invaild index")
        return self._A[k]

    def append(self, item):
        """
        向数组的末尾添加元素
        """
        if self._n == self._capacity:                     # 如果数组的容量不足（已满），2 倍扩大数组容量
            self._resize(2 * self._capacity)
        self._A[self._n] = item                           # 数组中添加元素
        self._n += 1                                      # 数组的元素计数器加 1
    
    def _resize(self, new_capacity):
        """
        重新调整数组的容量，其实就是重新在内存中开辟一个数组空间
        然后将当前数组中的元素的内存地址存储到新的数组中
        在将新的数组的内存地址与数组变量关联，当前数组会被垃圾回收掉
        """
        new_arrary = self._make_array(new_capacity)
        for k in range(self._n):
            new_arrary[k] = self._A[k]
        self._A = new_arrary
        self._capacity = new_capacity
    
    def _make_array(self, capacity):                      # 底层创建数组的私有方法
        """
        在内存中开辟一个空间，作为数组的存储空间

        >>> ctypes.py_object
        <class 'ctypes.py_object'>
        >>> ctypes.py_object()
        py_object(<NULL>)
        >>> ctypes.py_object(1)
        py_object(1)
        """
        # ctypes.py_object() 表示C 数据类型。在没有参数的情况下调用它会创建一个 NULL 指针。
        # NULL 是一个标准规定的宏定义，用来表示空指针常量。
        # 空指针表示“未分配”或者“尚未指向任何内存中的其他地方”
        return (capacity * ctypes.py_object)()
