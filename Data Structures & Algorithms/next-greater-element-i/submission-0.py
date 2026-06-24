class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        for i in range(len(nums2)):
            hmap[nums2[i]] = i
        out = []
        for i in nums1:
            ng = -1
            for j in range(hmap[i]+1,len(nums2)):
                if nums2[j] > i:
                    ng = nums2[j]
                    out.append(ng)
                    break
            if ng == -1:
                out.append(ng)
        return out