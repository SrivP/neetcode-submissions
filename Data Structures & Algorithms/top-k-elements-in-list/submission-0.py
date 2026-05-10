class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        ans = []
        for n in nums:
            res[n] += 1
        sorted_values = sorted(list(res.values()), reverse=True)[0:k]
        for n in (res.keys()):
            for ele in sorted_values:
                if res.get(n) == ele:
                    ans.append(n)
        return list(set(ans))