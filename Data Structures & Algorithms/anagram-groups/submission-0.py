class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use hash table. a dictionary with key the alphabets. 
        #turn each str to a dict
        #compare dicts? Go through list?
        
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())