class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        G,B = 1,2
        G = defaultdict(set)
        for s,e in edges:
          G[s].add(e)
          
        def dfs(cur, states)->bool:
          if states[cur]:
            return states[cur] == B
          if len(G[cur]) == 0:
            return cur == destination
          
          states[cur] = G
          for neig in G[cur]:
            if not dfs(neig, states):
              return False
          states[cur] = B
          return True

        states = [None]*n
        return dfs(source, states)