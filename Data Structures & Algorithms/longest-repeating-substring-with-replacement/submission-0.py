class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        widic = {s[0]:1}
        maxl = 0
        max_count = 1
        total_count = 1

        while r < len(s)-1:
            
            r += 1
            widic[s[r]] = widic.get(s[r], 0) + 1
            max_count = max(max_count, widic[s[r]])
            total_count = sum(widic.values())

            if (total_count - max_count) <= k:
                maxl = max(maxl, r - l + 1)
            else: 
                while (total_count - max_count) > k:
                    widic[s[l]] = max(widic[s[l]]-1, 0)
                    l += 1
                    max_count = max(widic.values())
                    total_count = sum(widic.values())
                
            

        return maxl
            


        