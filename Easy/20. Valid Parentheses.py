class Solution:
    def isValid(self, s: str) -> bool:
        n = 0
       
        while len(s) != n:
            n = len(s)
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
       
        if len(s) == 0:
            return True
        else:
            return False
