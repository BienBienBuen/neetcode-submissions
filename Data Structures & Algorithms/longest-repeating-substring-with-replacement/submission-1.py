class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        widic = {}
        maxl = 0
        max_count = 0
        total_count = 0

        while r < len(s):
            
            widic[s[r]] = widic.get(s[r], 0) + 1
            max_count = max(max_count, widic[s[r]])
            total_count = (r - l + 1)

            while (total_count - max_count) > k:
                widic[s[l]] = max(widic[s[l]]-1, 0)
                l += 1
                total_count = (r - l + 1)

            maxl = max(maxl, r - l + 1)
            r += 1

        return maxl
            


        