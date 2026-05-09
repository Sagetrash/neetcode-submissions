class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        array = [(position[i],speed[i],int(target-position[i])/speed[i]) for i in range(len(position))]
        array = sorted(array)
        print(array)
        fleet = 0
        eta = 0
        while array:
            curr = array.pop()
            if curr[2] <= eta:
                continue
            else:
                eta = curr[2]
                fleet += 1
        return fleet
