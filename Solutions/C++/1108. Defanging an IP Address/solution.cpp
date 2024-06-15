class Solution {
public:
    string defangIPaddr(string address) {
        string newAddress;
        for (char c : address) { 
            if (c == '.') {
                newAddress += "[.]";
            } else {
                newAddress += c;
            }
        }
        return newAddress;
    }
};