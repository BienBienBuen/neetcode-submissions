class Solution:

    def is_number(self, s: str) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.is_number(token):
                stack.append(token)
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                result = int(eval(f"{n2} {token} {n1}"))
                stack.append(result)
        return int(stack[0])
