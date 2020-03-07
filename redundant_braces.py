class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        top = -1
        
        # push operands and ( in stack and pop till ( is found if ) is encountered
        for i in range(len(A)):
            if A[i] in ('+', '-', '*', '/', '('):
                stack.append(A[i])
                top += 1
                # print('after insertion stack = ',stack,' and top = ',top)
            if A[i] == ')':
                if stack[top] == '(':
                    return 1
                else:
                    for j in range(len(stack)):
                        if stack[top] == '(':
                            stack.pop()
                            top -= 1
                            break
                        stack.pop()
                        top -= 1
                        # print('stack after pop = ',stack,' top = ',top)
                        
        if top == -1:
            return 0
        else:
            if '(' in stack or ')' in stack:
                return 1
            else:
                return 0
