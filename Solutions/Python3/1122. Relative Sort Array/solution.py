class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        priority = {}
        for i, num in enumerate(arr2):
            priority[num] = i

        min_other_order = len(arr2)

        arr1.sort(key=lambda item: priority.get(item, item+min_other_order))
        return arr1