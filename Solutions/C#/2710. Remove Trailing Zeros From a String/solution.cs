public class Solution {
    public string RemoveTrailingZeros(string num) {
        int i;
        for (i = num.Length - 1; i >= 0; i--) {
            if (num[i] != '0') {
                break;
            }
        }
        
        return num.Substring(0, i + 1);
    }
}