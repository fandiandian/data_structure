#! /usr/bin/env python3
# _*_ coding: utf-8 _*_


class Tree:
    """Abstract base class representing a tree structure."""

    # --------------------------- nested Position class ------------------------
    class Position:
        """An abstract representing the location of a single element"""

        def element(self):
            """Return the element stored at this Positon."""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """Return True if other Position represent is the same location."""
            raise NotImplementedError("must be implemented bu subclass")

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            raise NotImplementedError("must be implemented by subclass")

    # -------- abstract methods that concrete subclass must support ---------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """Return Position representing p's parent (or None p is root)."""
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """Return the number of children the Position p has."""
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """Generate an iteration of Position representing p's children."""
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """Return the total number of elements is in the tree."""
        raise NotImplementedError("must be implemented by subclass")

    # -------- concrete methods implemented in the class ---------
    def is_root(self, p):
        """Return True if Position p represent the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0
