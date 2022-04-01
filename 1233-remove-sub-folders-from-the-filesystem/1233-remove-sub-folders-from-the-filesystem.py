class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = {}

        def insert(s):
            cur = root
            for c in s.split("/"):
                cur = cur.setdefault(c, {})
            cur["#"] = s

        for f in folder:
            insert(f)

        # find every paths
        def bt(cur, path, res):
            if not cur or "#" in cur:
                res.append("/".join(path))
                return
            for c in cur:
                bt(cur[c], path + [c], res)

        res = []
        bt(root, [], res)
        return res