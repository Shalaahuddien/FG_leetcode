# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        def dfs(q):
            # deque of nums, +, - nodes
            deq = deque()
            while q:
                c = q.popleft()
                if c.isdigit():
                    deq.append(Node(c))
                elif c == "(":
                    sub = dfs(q)
                    deq.append(sub)
                elif c == ")":
                    break
                elif c in "+-":
                    deq.append(Node(c))
                else:  # c in '*/'
                    node = Node(c)
                    node.left = deq.pop()
                    next = q.popleft()
                    if next == "(":
                        node.right = dfs(q)
                    else:
                        node.right = Node(next)
                    deq.append(node)

            root = deq.popleft()
            while deq:
                node = deq.popleft()
                node.left = root
                node.right = deq.popleft()
                root = node
            return root

        q = deque(s)
        return dfs(q)