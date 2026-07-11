class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #recursive? use sol of n-1
        output = []
        stack = [("", 0, 0)]
        while stack:
            parenthesis, left_count, val = stack.pop()
            if len(parenthesis) == 2*n:
                output.append(parenthesis)
            else:
                if val > 0:
                    if left_count < n:
                        left = parenthesis + "("
                        right = parenthesis + ")"
                        stack.append((left, left_count+1, val + 1))
                        stack.append((right, left_count, val - 1))
                    else:
                        right = parenthesis + ")"
                        stack.append((right, left_count, val - 1))
                elif val == 0:
                    left = parenthesis + "("
                    stack.append((left, left_count+1,val+1))
        return output
        