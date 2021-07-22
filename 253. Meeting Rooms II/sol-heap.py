class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        maxheap: heapq func 放東西時都要 * -1
        '''
        
        intervals = sorted(intervals, key=lambda l:l[0])
        print(intervals)
        
        maxroom = 0
        ongoing = [inf]
        heapq.heapify(ongoing)
        
        for start, end in intervals:
            
            # check if ongoing conference ends when the meeting starts
            while start >= ongoing[0]:
                heapq.heappop(ongoing)
            
            # a new conference is ongoing
            heapq.heappush(ongoing, end)
            
            # update nums of ongoing meeting
            maxroom = max(maxroom, len(ongoing))
            # print(f'{ongoing}, {start}, {end}')
        
        
        return maxroom - 1
        
        heapq.heappush(ongoing, -5)
        # print(ongoing)
    
        
