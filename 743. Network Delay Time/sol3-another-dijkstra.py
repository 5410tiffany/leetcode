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
        # start from origin
        pq = [(0,k)]
        self.mindist[k] = 0
        
        while pq:
            # visit node with shortest distance
            dist, node = heapq.heappop(pq)
            # print(f'{dist}, {node}, {self.mindist[node]}')
            
            # don't need to continue traversing if got a better path-> this is not necessary
            if self.mindist[node] < dist: continue    
                
            # update mindist    
            self.mindist[node] = min(dist, self.mindist[node])
            
            # relax node's neighbor who hasn't visited before and put them into pq
            for dest, w in self.G[node]: 
                if self.mindist[dest] == float('inf'):
                    heapq.heappush(pq, (w+dist, dest))
                # print(pq)
            
            
        # print(f'{self.mindist}')
        ans = max(self.mindist.values())
            
        return ans if ans < float('inf') else -1
