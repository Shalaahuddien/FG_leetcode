class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dfs = [0]
        seen = set(dfs)
        while dfs:
            cur = dfs.pop()
            for j in rooms[cur]:
                if j not in seen:
                    dfs.append(j)
                    seen.add(j)
                    # prune as soon as visited all rooms
                    if len(seen) == len(rooms):
                        return True
        return len(seen) == len(rooms)