class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #take length of s1, hash every substr len 1 in second in a set. 
        l1 = len(s1)
        l2 = len(s2)
        count = l2 - l1 + 1
        hasu = set()
        if count < 1:
            return False
        for i in range(count):
            sliced = s2[i:i+l1]
            ls = [0]*26
            for char in sliced:
                asc = ord(char) - ord('a')
                ls[asc] += 1
            hasu.add(tuple(ls))
        
        ls = [0]*26
        for char in s1:
            asc = ord(char) - ord('a')
            ls[asc] += 1
        if tuple(ls) in hasu:
            return True
        else:
            return False


        