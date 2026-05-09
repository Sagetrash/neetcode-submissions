class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        array = [(position[i],speed[i],(target-position[i])/speed[i]) for i in range(len(position))]
        array.sort()
        fleet = 0
        eta = 0
        while array:
            curr = array.pop()
            if curr[2] <= eta:
                continue
            else:
                fleet += 1
                eta = curr[2]
        return fleet