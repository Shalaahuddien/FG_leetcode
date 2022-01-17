class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        ind = [0] * n
        for l, r in zip(leftChild, rightChild):
            if l != -1:
                ind[l] += 1
                if ind[l] > 1:
                    return False
            if r != -1:
                ind[r] += 1
                if ind[r] > 1:
                    return False

        if ind.count(0) != 1:
            return False

        # root's indegree === 0
        root = ind.index(0)

        # count nodes from root, if the total number is not n, it means there are islands, then return false.
        def count_nodes(r):
            if r == -1:
                return 0
            return 1 + count_nodes(leftChild[r]) + count_nodes(
                rightChild[r])

        nodes = count_nodes(root)
        return nodes == n