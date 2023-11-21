class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        
        critical_points = []
        
        boundaries = []
        for left, right, height in buildings:
            boundaries.append((left, -height, right))
            boundaries.append((right, 0, 0))
        
        boundaries.sort()
        
        max_heap = [(0, float('inf'))]
        
        for x, neg_height, right in boundaries:
            if neg_height == 0:
                while max_heap and max_heap[0][1] <= x:
                    heapq.heappop(max_heap)
            else:
                heapq.heappush(max_heap, (neg_height, right))
            
            max_height = -max_heap[0][0]
            
            if not critical_points or max_height != critical_points[-1][1]:
                critical_points.append([x, max_height])
        
        return critical_points