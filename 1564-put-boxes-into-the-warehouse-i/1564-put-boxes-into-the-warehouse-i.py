class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)
        i, count = 0, 0
        for r in warehouse:
            while i < len(boxes) and boxes[i] > r:
                i += 1
            if i == len(boxes):
                return count
            count += 1
            i += 1
        return count