class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        G = defaultdict(list)
        for i, v in enumerate(arr):
            G[v].append(i)

        step = 0
        front, end = set([0]), set([n - 1])
        vis = set([0, n - 1])
        while front:
            # search from the side with fewer nodes
            if len(front) > len(end):
                front, end = end, front

            front_next = set()
            for cur in front:
                '''
                24 / 32 test cases passed: [-76,3,66,-32,64,2,-19,-8,-5,-93,80,-5,-76,-78,64,2,16]

                BUG: if pop from set, not in order, so the qlen trick doesn't work! Have to use another set to save front's expand!
                cur = front.pop()
                '''
                v = arr[cur]

                # option 3
                for i in G[v]:
                    if i in end:
                        return step + 1
                    if i not in vis:
                        vis.add(i)
                        front_next.add(i)

                # clear the list to prevent redundant search
                # del G[v]
                G[v].clear()

                # option 1,2
                for i in {cur - 1, cur + 1}:
                    if i in end:
                        return step + 1
                    if 0 <= i < n and i not in vis:
                        vis.add(i)
                        front_next.add(i)

            front = front_next
            step += 1
        return -1