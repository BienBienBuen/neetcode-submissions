class Solution:
    def isValid(self, s: str) -> bool:
        #use the stack architecture
        left = {"{","[","("}
        right = {"}", "]", ")"}
        pairing = {"}": "{", 
                    "]": "[",
                    ")": "("}
        stack = []
        for letter in s:
            if letter in left:
                stack.append(letter)
            elif letter in right:
                if not stack:
                    return False
                if pairing[letter] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False

        