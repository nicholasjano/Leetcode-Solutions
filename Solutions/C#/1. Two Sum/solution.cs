public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> storage = new Dictionary<int, int>();
        int[] array1 = new int[2];

        for (int i = 0; i < nums.Length; i++)
        {
            if (storage.ContainsKey(target - nums[i]))
            {
                array1[0] = storage[target - nums[i]];
                array1[1] = i;
                break;
            }
            else
            {
                storage[nums[i]] = i;
            }
        }
        return array1;
    }
}