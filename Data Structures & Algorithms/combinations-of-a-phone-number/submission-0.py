class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #dictionary mapped to a list?
        #dynamically solve this? we still have a digit, but build it up
        #step by step
        lookup = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno",
        '7':"pqrs", '8':"tuv", '9':"wxyz"}
        def construct(digits: str) -> List[str]:
            result = []
            if len(digits) == 0:
                return result
            elif len(digits) == 1:
                result = [s for s in lookup[digits]]
                return result
            else:
                prev_results = construct(digits[:-1])
                for prev in prev_results:
                    sub_result = [prev + s for s in lookup[digits[-1]]]
                    result += sub_result
                return result
        return construct(digits)
