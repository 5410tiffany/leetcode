class Solution:
    def networkDelayTime(self, times, n, k):
        '''
        Dijkstra: non-negative w
        times: weighted graph
        n: number of nodes
        k: origin
        '''
        # maintain mindist[n]: the shortest path from k -> n
        self.mindist = {node: float('inf') for node in range(1, n+1)}
        
        # tunr graph into adjacency list
        self.G = defaultdict(list)
        
        for src, dest, w in times:
            self.G[src].append((dest, w))
            # print(f'{src}, {dest}, {self.G[src]}')
            
        # priority queue: sort acording to distance
        
        pq = [(0,k)]
        
        while pq:
            dist, node = heapq.heappop(pq)
            # print(f'{dist}, {node}, {self.mindist[node]}')
            
            if self.mindist[node] < dist: continue
                
            self.mindist[node] = dist
            
            for dest, w in self.G[node]: # put node's neighbor into pq
                # print(f'{self.mindist[dest]},, {(self.mindist[node]+w)}')
                if self.mindist[dest] > (self.mindist[node]+w):
                    heapq.heappush(pq, (w+dist, dest))
                # print(pq)
            
            
        # print(f'{self.mindist}')
        ans = max(self.mindist.values())
            
        return ans if ans < float('inf') else -1
