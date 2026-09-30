class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_app = []
        appearance = defaultdict(int)
        for num in nums:
            appearance[num] += 1
        buckets = [[] for _ in range(len(nums)+1)]

        for num, count in appearance.items():
            buckets[count].append(num)
        
        res = []

        for i in range(len(buckets)-1,0,-1):
            for j in buckets[i]:
                res.append(j)
            if len(res) == k:
                break   
        return res

        




            

        