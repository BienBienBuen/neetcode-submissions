class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #have a dictionary for a specific window
        curr_dict: Dict[str:int] = {}
        target_dict = {}
        for letter in t:
            target_dict[letter] = target_dict.get(letter, 0) + 1
        
        l,r = 0,0
        min_length = float('inf')
        #keep track of pointer corresponding to min_length
        min_l = 0
        min_r = 0

        while r <= len(s):
            if all(curr_dict.get(ch, 0) >= target_dict[ch] for ch in target_dict):
                curr_length = r - l + 1
                if curr_length < min_length:
                    min_length = curr_length
                    min_l, min_r = l, r
                curr_dict[s[l]] -= 1
                if curr_dict[s[l]] < 0:
                    del curr_dict[s[l]]
                l+=1
            else:
                if r == len(s):
                    break
                curr_dict[s[r]] = curr_dict.get(s[r], 0) + 1
                r+=1
   
            
        return s[min_l: min_r]
