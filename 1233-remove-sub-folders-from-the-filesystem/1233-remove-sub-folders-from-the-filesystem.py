class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        for f in sorted(folder):
            if not ans or not f.startswith(ans[-1] + "/"):
                ans.append(f)
        return ans
