class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_set = defaultdict(int)

        for i in s:
            char_set[i] += 1
        print(char_set)
        for j in t:
            char_set[j] -= 1 
        print(char_set)
        for ch in char_set:
            if char_set[ch] != 0:
                return False
        
        return True
        
