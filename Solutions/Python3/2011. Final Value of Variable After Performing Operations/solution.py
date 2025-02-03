class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for operation in operations:
            if operation[1] == "+":
                X += 1
            else:
                X -= 1
        
        return X
        