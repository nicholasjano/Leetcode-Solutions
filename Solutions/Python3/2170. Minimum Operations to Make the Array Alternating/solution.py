class Solution:
    def getTopTwo(self, counter):
        top = None
        top_occurences = 0
        second = None
        second_occurences = 0
        for num, occurences in counter.items():
            if occurences > top_occurences:
                top, second = num, top
                top_occurences, second_occurences = occurences, top_occurences
            elif occurences > second_occurences:
                second = num
                second_occurences = occurences
        return [top, second]

    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return 0
            
        even_len = (n + 1) // 2
        odd_len = n // 2
        
        nums_even = []
        nums_odd = []

        for i in range(n):
            if i % 2 == 0:
                nums_even.append(nums[i])
            else:
                nums_odd.append(nums[i])
        
        even_counter = Counter(nums_even)
        odd_counter = Counter(nums_odd)
        
        even_top = self.getTopTwo(even_counter)
        odd_top = self.getTopTwo(odd_counter)
        
        if even_top[0] != odd_top[0]:
            return (even_len - even_counter[even_top[0]]) + (odd_len - odd_counter[odd_top[0]])
        
        even_keep_strategy = odd_len
        if odd_top[1] is not None:
            even_keep_strategy = (even_len - even_counter[even_top[0]]) + (odd_len - odd_counter[odd_top[1]])
        
        odd_keep_strategy = even_len
        if even_top[1] is not None:
            odd_keep_strategy = (even_len - even_counter[even_top[1]]) + (odd_len - odd_counter[odd_top[0]])
        
        return min(even_keep_strategy, odd_keep_strategy)
