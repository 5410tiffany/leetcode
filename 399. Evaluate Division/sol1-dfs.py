class Solution:
    def dfs(self, curr, target, acc):
        self.visited.add(curr)
        # self.instack.add(curr)
        
        for nei, w in self.G[curr]:
            # print(f'{curr}: {nei}, {w} || vis: {self.visited}')
            
            if nei in self.visited:
                print('visited!')
                continue
            
            elif nei == target:
                print('queried!')
                return acc*w
            
            else:
                self.visited.add(nei)
                ans = self.dfs(nei, target, acc*w)
                if ans!= -1: return ans
                
        # self.instack.remove(curr)
        return -1
    
    def calcEquation(self, equations, values, queries):
        '''
        turn eqs into graph, deal with queries one by one by finding the path btwn 2 nodes
        b.c: 
        node not in graph = -1
        node points to itself = 1
        '''
        
        # build bi-directional graph from equations 
        self.G = defaultdict(list)
        
        for (src, dest), w in zip(equations, values):
            # print(f'{src}, {dest}, {w} ')
            self.G[src].append((dest, w))
            self.G[dest].append((src, 1/w))
        
        print(self.G)
        
        
        # evaluate each query using dfs
        self.accprod = [1 for _ in range(len(queries)) ]
        # print(self.accprod)

        
        for i in range(len(queries)):
            src = queries[i][0]
            dest = queries[i][1]
            
            # BC: not in graph & point to itself 
            if src not in self.G or dest not in self.G:
                self.accprod[i] = -1.
            
            elif src == dest:
                self.accprod[i] = 1.
            
            else:
                self.visited = set()
                # self.instack = set()
                acc = 1
                self.accprod[i] = self.dfs(src, dest, acc)
                
        
        return self.accprod
        
