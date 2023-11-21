class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_time = 0
        
        for house in garbage:
            total_time += len(house)

        has_metal, has_paper, has_glass = False, False, False

        for i in range(len(travel), 0, -1):
            has_metal = has_metal or 'M' in garbage[i]
            has_paper = has_paper or 'P' in garbage[i]
            has_glass = has_glass or 'G' in garbage[i]

            total_time += travel[i-1] * (has_metal + has_paper + has_glass)
        
        return total_time