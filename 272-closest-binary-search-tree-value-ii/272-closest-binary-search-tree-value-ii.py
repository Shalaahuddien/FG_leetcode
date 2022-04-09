# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        def partition(pi, l, r):
            pivot_dist = dist(pi)

            # 1. move pivot to end
            nums[r], nums[pi] = nums[pi], nums[r]
            store_idx = l

            # 2. move more close elements to the left
            for i in range(l, r):
                if dist(i) < pivot_dist:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1

            # 3. move pivot to its final place
            nums[r], nums[store_idx] = nums[store_idx], nums[r]

            return store_idx

        def quickselect(left, right):
            """
            Sort a list within left..right till kth less close element
            takes its place.
            """
            # base case: the list contains only one element
            if left == right:
                return

            # select a random pivot_index
            pivot_idx = randint(left, right)

            # find the pivot position in a sorted list
            true_idx = partition(pivot_idx, left, right)

            # if the pivot is in its final sorted position
            if true_idx == k:
                return

            if true_idx < k:
                # go right
                quickselect(true_idx, right)
            else:
                # go left
                quickselect(left, true_idx)

        nums = inorder(root)
        dist = lambda idx: abs(nums[idx] - target)
        quickselect(0, len(nums) - 1)
        return nums[:k]