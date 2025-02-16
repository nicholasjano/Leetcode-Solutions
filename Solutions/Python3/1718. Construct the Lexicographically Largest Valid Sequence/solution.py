class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2 * (n - 1) + 1)
        used = set()

        def dfs(index=0):
            if index == len(res):
                return True
            
            if res[index] != 0:
                return dfs(index + 1)

            for num in range(n, 0, -1):
                if num in used:
                    continue

                if num == 1:
                    res[index] = 1
                    used.add(1)
                    if dfs(index + 1):
                        return True
                    res[index] = 0
                    used.remove(1)
                else:
                    if index + num < len(res) and res[index + num] == 0:
                        res[index] = num
                        res[index + num] = num
                        used.add(num)
                        if dfs(index + 1):
                            return True
                        res[index] = 0
                        res[index + num] = 0
                        used.remove(num)

            return False

        dfs()
        return res
