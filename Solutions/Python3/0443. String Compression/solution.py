class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 0:
            return 0
        
        write = 0
        count = 1
        
        for read in range(1, n + 1):
            if (read == n) or (chars[read - 1] != chars[read]):
                chars[write] = chars[read - 1]
                write += 1
                
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                
                count = 1
            else:
                count += 1
        
        return write