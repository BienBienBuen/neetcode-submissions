class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref = []
        suf = []
        for i in range(len(nums)):
            if i == 0:
                pref.append(1)
                suf.append(1)
            else:
                newpref = pref[i-1]*nums[i-1]
                pref.append(newpref)

                ng = -(i+1)
                newsuf = suf[ng+1]*nums[ng+1]
                suf.insert(0, newsuf)
        
        print(pref)
        print(suf)

        outputlist = result = [a * b for a, b in zip(pref, suf)]
        return outputlist
        