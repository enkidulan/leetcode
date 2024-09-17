class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            # print(i, stack)
            match i:
                case "+":
                    stack.append(stack.pop(-2) + stack.pop())
                case "-":
                    stack.append(stack.pop(-2) - stack.pop())
                case "*":
                    stack.append(stack.pop(-2) * stack.pop())
                case "/":
                    stack.append(int(stack.pop(-2) / stack.pop()))
                case _:
                    stack.append(int(i))
        return stack[0]
