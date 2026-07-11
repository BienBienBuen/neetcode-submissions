class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        target = {}
        for ch in t:
            target[ch] = target.get(ch, 0) + 1
        
        window = {}
        have, need = 0, len(target)
        l = 0
        min_len = float('inf')
        min_start = 0
        
        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1
            
            if ch in target and window[ch] == target[ch]:
                have += 1
            
            while have == need:
                # Update answer
                curr_len = r - l + 1
                if curr_len < min_len:
                    min_len = curr_len
                    min_start = l
                
                # Shrink from left
                left_char = s[l]
                window[left_char] -= 1
                if left_char in target and window[left_char] < target[left_char]:
                    have -= 1
                l += 1
        
        return s[min_start:min_start + min_len] if min_len != float('inf') else ""    