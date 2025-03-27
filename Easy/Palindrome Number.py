class Solution:
    """
    Converts the int to a string, checks if it's equal to the reverse of the string. 
    Returns true/false
    """
    def isPalindrome(self, x: int) -> bool:
        integer = []
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False