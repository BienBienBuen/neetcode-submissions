class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #two pointer, hashing the sliced string
        if len(s) <= 1:
            return len(s)

        l = 0
        r = 0

        hasu = {s[0]:1}
        maxl = 1

        while r < len(s) - 1:
            r += 1
            if s[r] in hasu:
                while s[r] in hasu:
                    del hasu[s[l]]
                    l += 1
                hasu[s[r]] = 1
                maxl = max(r - l + 1, maxl)
            else:
                hasu[s[r]] = 1
                maxl = max(r - l + 1, maxl)
        return maxl


        