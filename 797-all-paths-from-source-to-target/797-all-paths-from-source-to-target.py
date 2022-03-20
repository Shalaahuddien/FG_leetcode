class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        def bt(cur, path, res):
            if cur == n-1:
                res.append(path[:])
                return
            for nei in graph[cur]:
                bt(nei, path+[nei], res)
                
        res = []
        bt(0, [0], res)
        return res