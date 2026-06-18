class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        array = [(position[i],speed[i],(target-position[i])//speed[i]) for i in range(len(position))]
        array = sorted(array)
        print(array)
        fleet = 1
        eta = array[-1][2]
        while array:
            curr = array.pop()
            if array and curr[2] <= eta:
                array.pop()
            else:
                fleet += 1
        return fleet
