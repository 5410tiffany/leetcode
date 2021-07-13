class Solution:
    def dfs(self, node, elapsed):
        '''
        node: source
        elapsed: current time spent from origin
        '''
        if elapsed >= self.dist[node]: 
            # print(f'{node}, {self.dist[node]}')
            return
        self.dist[node] = elapsed
        
        for dest, w in self.G[node]:
            # print(f'{dest}, {elapsed+w}')
            self.dfs(dest, elapsed + w)
        return 
    
    def networkDelayTime(self, times, n, k):
        '''
        times: weighted graph
        n: number of nodes
        k: origin
        
        '''
        # maintain dist[n]: the shortest path from k -> n
        self.dist = {node: float('inf') for node in range(1, n+1)}
        # print(self.dist)
        
        # tunr graph into adjacency list
        self.G = defaultdict(list)
        
        for src, dest, w in times:
            self.G[src].append((dest, w))
            # print(f'{src}, {dest}, {self.G[src]}')
            
        
        self.dfs(k, 0)
        
        ans = max(self.dist.values())
        print(self.dist)
        
        return ans if ans < float('inf') else -1
        
