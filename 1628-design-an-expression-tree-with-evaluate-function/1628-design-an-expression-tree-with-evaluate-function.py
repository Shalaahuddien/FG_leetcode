from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


class TreeNode(Node):
    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        elif self.val == "*":
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == "+":
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == "-":
            return self.left.evaluate() - self.right.evaluate()
        else:
            return self.left.evaluate() // self.right.evaluate()

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> "Node":
        cur, stack = None, []
        for c in postfix:
            cur = TreeNode(c)
            if not c.isdigit():
                cur.right = stack.pop()
                cur.left = stack.pop()
            stack.append(cur)
        return cur