class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        


        map = [0] * 26 

        for i in s:
            map[ord(i) - ord('a')] += 1
        for j in t:
            map[ord(j) - ord('a')] -= 1

        for k in map:
            if k != 0:
                return False
        
        return True