class Solution:
    def trap(self, height: List[int]) -> int:
        water = height[:]
        k = 1
        i = k-1
        j = k+1
        while j < len(height):
            if height[k] < height[j] or height[k] < height[i]:
                if height[i] >= height[j]:
                    for l in range(i+1,j):
                        water[l] = height[j]
                    k += 1
                    if height[i] == height[j]:
                        i = k-1
                    j = k+1
                    continue
                else:
                    water[k] = height[i]
                    k+=1
                    i=k-1
                    j = k+1
            else:
                k += 1
                i = k-1
                j = k+1
        for i in range(len(height)):
            diff = water[i] - height[i]
            if diff >=0:
                water[i] = diff
            else:
                water[i] = 0
        return sum(water)