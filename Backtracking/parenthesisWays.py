class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        if expression.isdigit():
            return [int(expression)]

        answer = []
        op = "+-*"
        for idx, char in enumerate(expression):
            if char in op:
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx+1:])
                for leftNum in left:
                    for rightNum in right:
                        if char == "+": answer.append(leftNum + rightNum)
                        elif char == "-": answer.append(leftNum - rightNum)
                        else: answer.append(leftNum * rightNum)
        return answer