class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #one needs to keep track of the max of the list
        #when new max appears, old max gets updated. 
        #we need a max since every node?
        output = [0 for temp in temperatures]
        stack = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            temp, index = stack[-1]
            curr_temp = temperatures[i]
            if curr_temp <= temp:
                stack.append((temperatures[i], i))
            else:
                while len(stack) >= 1 and curr_temp > stack[-1][0]:
                    temp, index = stack.pop()
                    output[index] = i - index
                stack.append((temperatures[i], i))

        return output



            

        