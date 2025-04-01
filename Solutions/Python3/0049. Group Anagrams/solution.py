class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            key_count = tuple(count)
            if key_count in result:
                result[key_count].append(s)
            else:
                result[key_count] = [s]
        
        result_list = []
        for value in result.values():
            result_list.append(value)
        return result_list
