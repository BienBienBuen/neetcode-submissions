class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

    #     #method 1:
    #     #count freq, create dict, sort via this dict
    #     freq_dict = {}
    #     for num in nums:
    #         freq_dict[num] = freq_dict.get(num, 0) + 1
        
    #     print(freq_dict)
    #     output_list = []
    #     for key, item in freq_dict.items():

    #         if not output_list:
    #             output_list.append(key)

    #         else:
    #             added=False

    #             for j in range(len(output_list)):
    #                 if freq_dict[output_list[j]] <= item:
    #                     output_list.insert(j, key)
    #                     added = True
    #                     break
    #             if added == False:
    #                 output_list.append(key)

    #     print(output_list)          
    #     return output_list[:k]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res                




