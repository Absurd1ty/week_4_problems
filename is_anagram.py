"""Given two strings s and t , write a function to determine if t is an anagram of s."""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #new_str = ''.join(sorted(org_str))
        
        s1 = ''.join(sorted(s))
        t1 = ''.join(sorted(t))
        
        return s1 == t1